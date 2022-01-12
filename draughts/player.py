from abc import ABC, abstractmethod
from typing import Tuple, Type

from draughts.display import AbstractDisplay
from draughts.draughts import Draughts
from draughts.board import Board

from draughts_bots.abstract_bot import AbstractBot


class AbstractPlayer(ABC):
    """
    Abstract base class which all player classes must implement to ensure compatibility with the board and draughts
    classes.
    """
    @abstractmethod
    def __init__(self, name: str, game: Draughts, display: Type[AbstractDisplay]) -> None:
        self._name = name
        self._game = game
        self._display = display

    name = property(lambda self: self._name)

    @abstractmethod
    def get_move(self, valid_moves: Tuple[Tuple[int, int], ...]) -> Tuple[Tuple[int, int], Tuple[int, int]]: return

    @abstractmethod
    def accept_draw(self) -> bool: return

    @abstractmethod
    def move_accepted(self) -> None:
        self._update_display_board()

    @abstractmethod
    def win(self) -> None:
        self._update_display_winner()

    def get_board(self) -> Board:
        return self._game.get_board()

    def _update_display_board(self) -> None:
        if self._display:
            self._display.update_board()

    def _update_display_winner(self) -> None:
        if self._display:
            self._display.display_winner(self.name)
        else:
            print(f"{self.name} wins")


class HumanPlayer(AbstractPlayer):
    def __init__(self, name: str, display: Type[AbstractDisplay]) -> None:
        super().__init__(name, display)

    def get_move(self, valid_moves) -> Tuple[int, int]: return

    def accept_draw(self) -> bool: return

    def move_accepted(self) -> None: return

    def win(self) -> None: return


class BotPlayer(AbstractPlayer):
    def __init__(self, name: str, display: Type[AbstractDisplay], bot: Type[AbstractBot], game: Draughts) -> None:
        super().__init__(name, display)
        self._bot = bot
        self._game = game

    def get_move(self, valid_moves) -> Tuple[(int, int), (int, int)]: return

    def accept_draw(self) -> bool: return

    def move_accepted(self) -> None: return

    def win(self) -> None: return
