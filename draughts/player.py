from abc import ABC, abstractmethod
from typing import Tuple

from draughts.display import AbstractDisplay
from draughts.draughts import Draughts, Move, Position
from draughts.board import Board

from draughts_bots.abstract_bot import AbstractBot


class AbstractPlayer(ABC):
    """
    Abstract base class which all player classes must implement to ensure compatibility with the board and draughts
    classes.
    """

    @abstractmethod
    def __init__(self, name: str, game: Draughts, display: AbstractDisplay) -> None:
        self._name = name
        self._game = game
        self._display = display

    name = property(lambda self: self._name)

    @abstractmethod
    def get_move(self, valid_moves: Tuple[Move, ...]) -> Move:
        return

    @abstractmethod
    def accept_draw(self) -> bool:
        return

    @abstractmethod
    def move_accepted(self) -> None:
        self._update_display_board()

    @abstractmethod
    def win(self) -> None:
        self._update_display_winner()

    @abstractmethod
    def draw(self) -> None:
        self._update_display_draw()

    def get_board(self) -> Board:
        return self._game.get_board()

    def _update_display_board(self) -> None:
        if self._display:
            board = self.get_board()
            self._display.update_board(board)

    def _update_display_winner(self) -> None:
        if self._display:
            self._display.display_winner(self.name)

    def _update_display_draw(self):
        if self._display:
            self._display.display_draw()


class HumanPlayer(AbstractPlayer):
    def __init__(self, name: str, game: Draughts, display: AbstractDisplay) -> None:
        super().__init__(name, game, display)

    def get_move(self, valid_moves: Tuple[Tuple[Tuple[int, int], Tuple[int, int]], ...]) -> Tuple[int, int]: return

    def accept_draw(self) -> bool: return

    def move_accepted(self) -> None: return

    def win(self) -> None: return

    def draw(self) -> None: return


class BotPlayer(AbstractPlayer):
    def __init__(self, name: str, display: AbstractDisplay, bot: AbstractBot, game: Draughts) -> None:
        super().__init__(name, game, display)
        self._bot = bot

    def get_move(self, valid_moves: Tuple[Tuple[Tuple[int, int], Tuple[int, int]], ...]) -> Tuple[(int, int)]: return

    def accept_draw(self) -> bool: return

    def move_accepted(self) -> None: return

    def win(self) -> None: return

    def draw(self) -> None: return
