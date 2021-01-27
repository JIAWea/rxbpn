from rx.core import typing
from rxbp.init.initsubscription import init_subscription
from rxbp.mixins.flowablemixin import FlowableMixin
from rxbp.subscriber import Subscriber
from rxbp.subscription import Subscription

from rxbpn.observable.createbufferobservable import CreateBufferObservable


class CreateFlowable(FlowableMixin):
    def __init__(
            self,
            observer: typing.Subscription,
            buffer_size: int = 1
    ):
        self._observer = observer
        self.buffer_size = buffer_size

    def unsafe_subscribe(self, subscriber: Subscriber) -> Subscription:
        return init_subscription(
            observable=CreateBufferObservable(
                source=self._observer,
                buffer_size=self.buffer_size,
                scheduler=subscriber.scheduler,
                subscribe_scheduler=subscriber.subscribe_scheduler,
            )
        )
