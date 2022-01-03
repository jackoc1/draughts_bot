from draughts.board import Board, Piece


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
    turncount = property(lambda self: self._turn_count)

    def valid_moves(self, player):  # player 1 == 0, player 2 colour == 1
        pass

    def get_player_move(self):
        pass

    def _next_turn(self):
        pass

    def _valid_moves(self, player):
        pass

    def _valid_captures(self, player):
        pass

    def _move(self, piece, position):  # likely will delete
        pass

    def _capture(self, piece, position):  # likely will delete
        pass
