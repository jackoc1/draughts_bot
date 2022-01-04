from draughts.player_interface import PlayerInterface
from draughts.terminal_display import TerminalDisplay
from draughts.graphical_display import GraphicalDisplay  # Do over sequence diagram


class HumanPlayer(PlayerInterface):
    def __init__(self, display):
        self._display = display

    display = property(lambda self: self._display)

    def get_move(self):
        pass

    def forfeit(self):
        pass

    def offer_draw(self):
        pass

    def _get_move_terminal(self):
        pass

    def _get_move_graphical(self, event):
        pass

    def _forfeit_terminal(self):
        pass

    def _forfeit_graphical(self, event):
        pass

    def _offer_draw_terminal(self, event):
        pass

    def _offer_draw_graphical(self, event):
        pass
