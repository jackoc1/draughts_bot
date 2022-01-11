import tkinter as tk
from abc import ABC, abstractmethod

from draughts.draughts import Draughts


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


class GraphicalDisplay:
    def __init__(self, game, player_1_colour, player_2_colour, light_square_colour, dark_square_colour, bg_colour):
        self._game = game
        self._colours = {"player_1_pieces": player_1_colour, "player_2_pieces": player_2_colour,
                         "light_squares": light_square_colour, "dark_squares": dark_square_colour, "bg": bg_colour}

    def update_board(self):
        pass

    def player_input(self):
        pass

    def highlight_available_moves(self):
        pass

    def highlight_available_captures(self):
        pass

    def toggle_clickable(self):
        pass

    def display_winner(self):
        pass


class TerminalDisplay:
    def __init__(self, game, empty_square_character):
        self._game = game
        self._empty_square_character = empty_square_character

    def print_board(self):
        pass

    def player_input(self):
        pass

    def print_available_moves(self):
        pass

    def print_available_captures(self):
        pass

    def print_winner(self):
        pass
