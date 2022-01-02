from draughts.board import Board


class Draughts:
    def __init__(self, player_1, player_2):
        self._board = Board()
        self._player_1 = player_1  # import different class based on command line arguments
        self._player_2 = player_2
        self._active_player = player_1

    board = property(lambda self: self._board)
    player_1 = property(lambda self: self._player_1)
    player_2 = property(lambda self: self._player_2)
    active_player = property(lambda self: self._active_player)

    def valid_moves(self, colour):  # player 1 colour == 0, player 2 colour == 1
        pass

    def valid_captures(self, colour):
        pass

    def get_player_move(self):
        pass

    def get_player_capture(self):
        pass

    def next_turn(self):
        pass

    def _move(self, piece, position):
        pass

    def _capture(self, piece, position):
        pass
