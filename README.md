# rxbpn
rxbpn is an extension to the [rxbp](https://github.com/MichaelSchneeberger/rxbackpressure) which is back-pressure version of [RxPy](https://github.com/ReactiveX/RxPY).

# Example
Create a `Flowable` like `rx.create`.
```example
import rxbpn
from rxbpn import operators as op
from rxbpn.rx import Disposable, Observer
from rxbpn.scheduler import Scheduler
from rxbpn.testing.tobserver import TASubscribe

def handler(observer: Observer, scheduler: Scheduler):
    for i in range(10):
        observer.on_next([i])
    observer.on_completed()
    return Disposable()

publisher = rxbpn.create(handler).pipe(
    op.map(lambda v: v * 2),
    op.last(),
).subscribe(print)
```

# TODO
- [ ] Restart receiver
- [ ] RequestN