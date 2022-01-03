from draughts.board import Board


class Draughts:
    def __init__(self, player_1, player_2):
        self._board = Board()
        self._player_1 = player_1  # import different class based on command line arguments
        self._player_2 = player_2
        self._active_player = player_1
        self._turn_count = 0

    board = property(lambda self: self._board)
    player_1 = property(lambda self: self._player_1)
    player_2 = property(lambda self: self._player_2)
    active_player = property(lambda self: self._active_player)
    turn_count = property(lambda self: self._turn_count)

    def play(self):
        pass

    def next_turn(self):
        pass

    @staticmethod
    def valid_moves(player, board):
        pass

    def _valid_moves(self, player):  # player 1 == 0, player 2 == 1
        pass

    def _valid_captures(self, player):
        pass
