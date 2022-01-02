import tkinter as tk

from draughts.draughts import Draughts


class GraphicalDisplay:
    def __init__(self, player_1_colour, player_2_colour):
        self._game = Draughts()
        self._colours = (player_1_colour, player_2_colour)

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
