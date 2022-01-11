from draughts.board import Board


class Draughts:
    def __init__(self, player_1, player_2):
        self._board = Board()
        self._player_1 = player_1  # import different classes based on command line arguments
        self._player_2 = player_2
        self._turn_count = 0

    player_1 = property(lambda self: self._player_1)
    player_2 = property(lambda self: self._player_2)
    turn_count = property(lambda self: self._turn_count)

    def get_board(self): return

    def new_game(self, swap_pieces): return

    @staticmethod
    def valid_moves(board): return

    def _next_turn(self): return

    @staticmethod
    def _valid_moves(board, turn_count): return

    @staticmethod
    def _valid_captures(board, turn_count): return


