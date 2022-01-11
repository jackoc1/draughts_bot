class Board:
    def __init__(self, num_rows=8, num_cols=8, sample_board=[]):
        self._board = [[0] * num_rows] * num_cols

    def move(self, start_position, end_position):
        pass

    def get_board(self):  # don't expose internals
        pass

    def get_player_pieces(self, player):
        pass

    def get_piece(self, position):
        pass

    def promote(self, piece):
        pass

    def add_piece(self, position):
        pass

    def remove_piece(self, position):
        pass

class Piece:
    def __init__(self, player):
        self._player = player
        self._promoted = False

    player = property(lambda self: self._player)
    promoted = property(lambda self: self._promoted)

    def promote(self):
        pass

    def __eq__(self, other_piece):
        pass
