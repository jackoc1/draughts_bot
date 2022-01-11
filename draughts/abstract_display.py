from abc import ABC, abstractmethod


class AbstractDisplay(ABC):
    """
    Abstract base class which all player classes must implement to ensure compatibility with the board and draughts
    classes.
    """
    @abstractmethod
    def update_board(self): return

    @abstractmethod
    def get_move(self): return

    @abstractmethod
    def display_winner(self, name): return
