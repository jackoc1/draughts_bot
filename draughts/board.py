from draughts.piece import Piece


class Board:
    def __init__(self):
        self._board = []

    board = property(lambda self: self._board)

    def move(self, piece, position):
        pass

    def capture(self, piece, position):
        pass

    def get_player_pieces(self, player):
        pass

    def get_piece(self, position):
        pass

    def _promote(self, piece):  # likely will delete
        pass
