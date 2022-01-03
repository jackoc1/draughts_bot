from abc import ABC, abstractmethod

"""
Abstract base class which all player classes must implement to ensure compatibility with the board and draughts classes.
"""
class PlayerInterface(ABC):
    @abstractmethod
    def get_move(self):
        pass

    @abstractmethod
    def forfeit(self):
        pass

    @abstractmethod
    def offer_draw(self):
        pass