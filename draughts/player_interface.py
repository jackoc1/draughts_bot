from abc import ABC, abstractmethod

def PlayerInterface(ABC):
    """

    :param ABC:
    :return:
    """

    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def _search(self):
        pass

    @abstractmethod
    def copy_board(self):
        pass