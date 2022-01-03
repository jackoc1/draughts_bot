from draughts.player_interface import PlayerInterface


class BotPlayer(PlayerInterface):
    def __init__(self, bot, game):
        self._bot = bot
        self._game = game
        self._board_copy = game.board.deepcopy()

    def get_move(self):
        pass

    def forfeit(self):
        pass

    def offer_draw(self):
        pass

    def _calculate_move(self):
        pass
