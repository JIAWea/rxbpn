from rx.core import typing
from rx.scheduler.scheduler import Scheduler
from rxbp.observable import Observable

from rxbpn.observable.internal.observe import Observe
from rxbpn.observer import Sink


class CreateBufferObservable(Observe, Observable):
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

        super().__init__(self.scheduler, self.subscribe_scheduler)
