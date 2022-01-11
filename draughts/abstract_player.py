from abc import ABC, abstractmethod


class AbstractPlayer(ABC):
    """
    Abstract base class which all player classes must implement to ensure compatibility with the board and draughts
    classes.
    """
    @abstractmethod
    def __init__(self, name, game, display):
        self._name = name
        self._game = game
        self._display = display

    name = property(lambda self: self._name)

    @abstractmethod
    def get_move(self, valid_moves): return

    @abstractmethod
    def accept_draw(self): return

    @abstractmethod
    def move_accepted(self): return

    @abstractmethod
    def win(self): return

    def _update_display_board(self):
        if self._display:
            self._display.update_board()

    def _update_display_winner(self):
        if self._display:
            self._display.display_winner(self.name)
        else:
            print(f"{self.name} wins")
