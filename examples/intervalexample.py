import time

import rxbpn
from rxbpn import operators as op
from rxbpn.testing.tobserver import TASubscribe, TBSubscribe


def main():
    publisher = rxbpn.interval(1).pipe(
        op.map(lambda v: "new value"),
    )
    d = publisher.subscribe(
        observer=TBSubscribe(5),
    )

    time.sleep(100)
    d.dispose()


if __name__ == '__main__':
    main()
