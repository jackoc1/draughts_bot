from draughts.player_interface import PlayerInterface
from draughts.terminal_display import TerminalDisplay
from draughts.graphical_display import GraphicalDisplay  # Do over sequence diagram


class HumanPlayer(PlayerInterface):
    def get_move(self):
        pass

    def get_capture(self):
        pass

    def forfeit(self):
        pass

    def offer_draw(self):
        pass

    def get_move_terminal(self):
        pass

    def get_move_graphical(self, event):
        pass
