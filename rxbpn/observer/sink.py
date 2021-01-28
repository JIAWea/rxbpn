from abc import abstractmethod


class Sink:
    @abstractmethod
    def continue_loop(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def get_queue(self):
        raise NotImplementedError

    @abstractmethod
    def get_last_ack(self):
        raise NotImplementedError

    @abstractmethod
    def get_measured_state(self):
        raise NotImplementedError

    @abstractmethod
    def get_buffer_size(self):
        raise NotImplementedError

    @abstractmethod
    def get_back_pressure(self):
        raise NotImplementedError
