from draughts.piece import Piece


class Board:
    def __init__(self):
        self._board = []

    board = property(lambda self: self._board)

    def move(self, start_position, end_position):
        pass

    def capture(self, start_position, end_position):
        pass

    def get_player_pieces(self, player):
        pass

    def get_piece(self, position):
        pass

    def _promote(self, piece):  # likely will delete
        pass
