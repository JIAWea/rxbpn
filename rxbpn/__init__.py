from rx.core import typing
from rxbp.flowable import Flowable

from rxbpn.flowable.createflowable import CreateFlowable
from rxbpn.flowable.intervalflowable import IntervalFlowable
from rxbpn.init.initcreateflowable import init_create_flowable


def create(observer: typing.Subscription) -> Flowable:
    return init_create_flowable(
        underlying=CreateFlowable(observer)
    )


def interval(period: typing.RelativeTime) -> Flowable:
    """Returns an observable sequence that produces a value after each period.

    .. marble::
        :alt: interval

        [  interval()   ]
        ---1---2---3---4--->

    Example:
        >>> res = rx.interval(1.0)

    Args:
        period: Period for producing the values in the resulting sequence
            (specified as a :class:`float` denoting seconds or an instance of
            :class:`timedelta`).

    Returns:
        An flowable sequence that produces a value after each period.
    """
    return init_create_flowable(
        underlying=IntervalFlowable(period)
    )
