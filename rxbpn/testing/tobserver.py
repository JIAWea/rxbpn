from rxbp.acknowledgement.acksubject import AckSubject
from rxbp.acknowledgement.continueack import continue_ack
from rxbp.observer import Observer as AckObserver


class TASubscribe(AckObserver):
    def on_next(self, value):
        if value[0] == 11:
            return AckSubject()

        print("Received: {}, type: {}".format(value, type(value)))
        return continue_ack

    def on_completed(self):
        print('Done!')

    def on_error(self, exc):
        print('Exception: ', exc)
