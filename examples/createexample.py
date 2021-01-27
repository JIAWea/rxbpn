import rxbp
from rx.core import Observer
from rx.disposable import Disposable
from rxbp.scheduler import Scheduler

import rxbpn
from rxbpn.testing.tobserver import TASubscribe


def main():
    def handler(observer: Observer, scheduler: Scheduler):
        for i in range(100):
            observer.on_next([i])
        observer.on_completed()
        return Disposable()

    publisher = rxbpn.create(handler).pipe(
        rxbp.op.map(lambda v: v * 2),
        rxbp.op.last(),
    )
    publisher.subscribe(
        observer=TASubscribe(),
    )


if __name__ == '__main__':
    # run()

    main()
