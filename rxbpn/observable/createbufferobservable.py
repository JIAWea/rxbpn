from rx.core import typing
from rx.scheduler.scheduler import Scheduler
from rxbp.observable import Observable
from rxbp.observerinfo import ObserverInfo

from rxbpn.observer import CreateBufferedObserver
from rxbpn.observer import Sink


class CreateBufferObservable(Observable):
    def __init__(
            self,
            source: typing.Subscription,
            scheduler: Scheduler,
            subscribe_scheduler: Scheduler,
            buffer_size: int,
    ):
        self.source = source
        self.scheduler = scheduler
        self.subscribe_scheduler = subscribe_scheduler
        self.buffer_size = buffer_size

        # A sink is be able to start loop after backpressure
        self.sink: Sink = Sink()

    def observe(self, observer_info: ObserverInfo):
        observer = CreateBufferedObserver(
            underlying=observer_info.observer,
            scheduler=self.scheduler,
            subscribe_scheduler=self.subscribe_scheduler,
            buffer_size=self.buffer_size,
        )

        self.sink = observer

        return self.source(observer, self.subscribe_scheduler)
