import unittest

from rxbp.acknowledgement.acksubject import AckSubject
from rxbp.acknowledgement.continueack import continue_ack
from rxbp.init.initobserverinfo import init_observer_info
from rxbp.observer import Observer as AckObserver
from rxbp.schedulers.trampolinescheduler import TrampolineScheduler

from rxbpn.observable.createbufferobservable import CreateBufferObservable
from rxbpn.rx import Disposable, Observer


class TestCreateBufferObservable(unittest.TestCase):
    def setUp(self) -> None:
        self.scheduler = TrampolineScheduler()

    def test_sink_continue_loop(self):
        received = []

        def _create(o: Observer, schedule=None):
            for i in range(7):
                o.on_next([i])
            o.on_completed()
            return Disposable()

        class TASubscribe(AckObserver):
            def on_next(self, value):
                if value[0] == 3:
                    return AckSubject()
                nonlocal received
                received += value
                return continue_ack

            def on_completed(self):
                pass

            def on_error(self, exc):
                pass

        source = CreateBufferObservable(
            source=_create,
            scheduler=self.scheduler,
            subscribe_scheduler=self.scheduler,
        )
        source.observe(init_observer_info(observer=TASubscribe()))

        self.assertEqual([0, 1, 2], received)

        source.sink.continue_loop()
        self.assertEqual([0, 1, 2, 4, 5, 6], received)
