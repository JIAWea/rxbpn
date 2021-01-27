from abc import abstractmethod


class Sink:
    @abstractmethod
    def continue_loop(self) -> None:
        raise NotImplementedError
