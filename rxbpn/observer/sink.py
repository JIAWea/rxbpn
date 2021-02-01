from abc import abstractmethod, ABC


class Sink(ABC):
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

    # @abstractmethod
    # def get_buffer_size(self):
    #     raise NotImplementedError

    @abstractmethod
    def get_back_pressure(self):
        raise NotImplementedError


class BaseSink(Sink):
    def continue_loop(self) -> None:
        pass

    def get_queue(self):
        pass

    def get_last_ack(self):
        pass

    def get_measured_state(self):
        pass

    def get_back_pressure(self):
        pass
