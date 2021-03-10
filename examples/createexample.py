import time

from rxbp.schedulers.threadpoolscheduler import ThreadPoolScheduler

import rxbpn
from rxbpn import operators as op
from rxbpn.rx import Disposable, Observer
from rxbpn.scheduler import Scheduler
from rxbpn.testing.tobserver import TBSubscribe


def main():
    def handler(observer: Observer, scheduler: Scheduler):
        for i in range(10):
            time.sleep(0.5)
            observer.on_next([i])
        observer.on_completed()
        # return Disposable()

    publisher = rxbpn.create(handler).pipe(
        op.map(lambda v: v * 2),
        # op.last(),
    )
    d = publisher.subscribe(
        # observer=TASubscribe(),
        observer=TBSubscribe(10),
        subscribe_scheduler=ThreadPoolScheduler("publisher")
    )

    time.sleep(0.9)
    d.dispose()
    time.sleep(100)


if __name__ == '__main__':
    main()
