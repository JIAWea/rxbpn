from rx.core import Observer
from rx.disposable import Disposable
from rxbp.acknowledgement.stopack import StopAck
from rxbp.scheduler import Scheduler

import rxbpn
from rxbpn.testing.tobserver import TASubscribe


def main():
    def handler(observer: Observer, scheduler: Scheduler):
        for i in range(100):
            ack = observer.on_next([i])

            if isinstance(ack, StopAck):
                break
        return Disposable()

    publisher = rxbpn.create(handler)
    publisher.subscribe(
        observer=TASubscribe(),
    )


if __name__ == '__main__':
    # run()

    main()
