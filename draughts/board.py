class Board:
    def __init__(self):
        self._board = [[0] * 8] * 8

    def move(self, start_position, end_position):
        pass

    def capture(self, start_position, end_position):
        pass

    def get_board(self):  # don't expose internals
        pass

    def get_player_pieces(self, player):
        pass

    def get_piece(self, position):
        pass

    def _promote(self, piece):  # likely will delete
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
