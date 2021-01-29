from typing import Optional

from rx.core import typing

from rxbpn.observable.internal import _timer


def _interval(period: typing.RelativeTime,
              scheduler: Optional[typing.Scheduler] = None
              ) -> typing.Subscription:
    return _timer(period, period, scheduler)
