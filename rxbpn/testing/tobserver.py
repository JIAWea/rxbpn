import threading

from rxbp.acknowledgement.acksubject import AckSubject
from rxbp.acknowledgement.continueack import continue_ack
from rxbp.acknowledgement.stopack import stop_ack
from rxbp.observer import Observer as AckObserver
from rxbp.typing import ElementType


class TASubscribe(AckObserver):
    def on_next(self, value):
        # if value[0] == 11:
        #     return AckSubject()

        print("Received: {}, type: {}".format(value, type(value)))
        return continue_ack

    def on_completed(self):
        print('Done!')

    def on_error(self, exc):
        print('Exception: ', exc)


class TBSubscribe(AckObserver):
    def __init__(self, num: int = None):
        self.received = []
        self.request_n = num or 256
        self.exception = None

        # counts the number of times `on_next` is called
        self.on_next_counter = 0

    def on_next(self, elem: ElementType):
        try:
            values = list(elem)
        except Exception as exc:
            self.exception = exc
            return stop_ack

        for v in values:
            print("Received: ", v)
            # print("thread: {}, received: {}".format(threading.current_thread().name, v))
        self.on_next_counter += 1

        if self.on_next_counter < self.request_n:
            return continue_ack
        else:
            return AckSubject()

    def on_error(self, exc):
        print('Exception: ', exc)

    def on_completed(self):
        print('Done!')
