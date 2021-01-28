import rxbpn
from rxbpn import operators as op
from rxbpn.rx import Disposable, Observer
from rxbpn.scheduler import Scheduler
from rxbpn.testing.tobserver import TASubscribe


def main():
    def handler(observer: Observer, scheduler: Scheduler):
        for i in range(100):
            observer.on_next([i])
        observer.on_completed()
        return Disposable()

    publisher = rxbpn.create(handler).pipe(
        op.map(lambda v: v * 2),
        op.last(),
    )
    publisher.subscribe(
        observer=TASubscribe(),
    )


if __name__ == '__main__':
    main()
