from typing import Any

from rx.core import typing, abc
from rx.core.observer import AutoDetachObserver
from rx.disposable import Disposable
from rx.scheduler import CurrentThreadScheduler
from rx.scheduler.scheduler import Scheduler
from rxbp.observable import Observable
from rxbp.observerinfo import ObserverInfo

from rxbpn.observer import BufferedObserver
from rxbpn.observer import Sink


class CreateBufferObservable(Observable):
    def __init__(
            self,
            source: typing.Subscription,
            scheduler: Scheduler,
            subscribe_scheduler: Scheduler,
    ):
        self.source = source
        self.scheduler = scheduler
        self.subscribe_scheduler = subscribe_scheduler

        # A sink is be able to start loop after backpressure
        self.sink: Sink = Sink()

    def observe(self, observer_info: ObserverInfo):
        observer = BufferedObserver(
            underlying=observer_info.observer,
            scheduler=self.scheduler,
            subscribe_scheduler=self.subscribe_scheduler,
        )

        self.sink = observer

        auto_detach_observer = AutoDetachObserver(
            observer.on_next,
            observer.on_error,
            observer.on_completed
        )

        def fix_subscriber(subscriber):
            """Fixes subscriber to make sure it returns a Disposable instead
            of None or a dispose function"""
            if not hasattr(subscriber, 'dispose'):
                subscriber = Disposable(subscriber)

            return subscriber

        def set_disposable(_: abc.Scheduler = None, __: Any = None):
            try:
                subscriber = self.source(auto_detach_observer, self.subscribe_scheduler)
            except Exception as ex:  # By design. pylint: disable=W0703
                if not auto_detach_observer.fail(ex):
                    raise
            else:
                auto_detach_observer.subscription = fix_subscriber(subscriber)

        # Subscribe needs to set up the trampoline before for subscribing.
        # Actually, the first call to Subscribe creates the trampoline so
        # that it may assign its disposable before any observer executes
        # OnNext over the CurrentThreadScheduler. This enables single-
        # threaded cancellation
        # https://social.msdn.microsoft.com/Forums/en-US/eb82f593-9684-4e27-
        # 97b9-8b8886da5c33/whats-the-rationale-behind-how-currentthreadsche
        # dulerschedulerequired-behaves?forum=rx
        current_thread_scheduler = CurrentThreadScheduler.singleton()
        if current_thread_scheduler.schedule_required():
            current_thread_scheduler.schedule(set_disposable)
        else:
            set_disposable()

        # Hide the identity of the auto detach observer
        return Disposable(auto_detach_observer.dispose)
