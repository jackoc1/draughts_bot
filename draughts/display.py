import tkinter as tk
from abc import ABC, abstractmethod
from typing import Tuple

from draughts.board import Board


class AbstractDisplay(ABC):
    """
    Abstract base class which all player classes must implement to ensure compatibility with the board and draughts
    classes.
    """
    @abstractmethod
    def update_board(self, board: Board) -> None: return

    @abstractmethod
    def get_move(self, valid_moves: Tuple[Tuple[int, int], ...]) -> Tuple[int, int]: return

    @abstractmethod
    def display_winner(self, name: str) -> None: return


class GraphicalDisplay:
    def __init__(self, player_1_colour: str, player_2_colour: str, light_square_colour: str,
                 dark_square_colour: str, bg_colour: str) -> None:
        self._colours = {"player_1_pieces": player_1_colour, "player_2_pieces": player_2_colour,
                         "light_squares": light_square_colour, "dark_squares": dark_square_colour, "bg": bg_colour}

    def update_board(self, board: Board) -> None:
        pass

    def get_move(self, valid_moves: Tuple[Tuple[int, int], ...]) -> Tuple[int, int]:
        pass

    def display_winner(self, name: str) -> None:
        pass

    def _highlight_available_moves(self) -> None:
        pass

    def _highlight_selected_piece(self) -> None:
        pass


class TerminalDisplay:
    def __init__(self, empty_square_character: str):
        self._empty_square_character = empty_square_character

    def update_board(self, board: Board) -> None:
        pass

    def get_move(self, valid_moves: Tuple[Tuple[int, int], ...]) -> Tuple[int, int]:
        pass

    def display_winner(self, name: str) -> None:
        pass

    def _print_available_moves(self) -> None:
        pass
