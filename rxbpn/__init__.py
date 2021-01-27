from rx.core import typing
from rxbp.flowable import Flowable

from rxbpn.flowable.createflowable import CreateFlowable
from rxbpn.init.initcreateflowable import init_create_flowable


def create(observer: typing.Subscription) -> Flowable:
    return init_create_flowable(
        underlying=CreateFlowable(observer)
    )
