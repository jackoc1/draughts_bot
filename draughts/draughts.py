from typing import Tuple, List

from draughts.board import Board


class Draughts:
    def __init__(self, player_1, player_2) -> None:
        self._board = Board()
        self._player_1 = player_1  # import different classes based on command line arguments
        self._player_2 = player_2
        self._turn_count = 0

    player_1 = property(lambda self: self._player_1)
    player_2 = property(lambda self: self._player_2)
    turn_count = property(lambda self: self._turn_count)

    def get_board(self) -> None: return

    def new_game(self, swap_pieces: bool) -> None: return

    @staticmethod
    def valid_moves(board: Board) -> Tuple[((int, int), (int, int))]: return

    @staticmethod
    def create_custom_board(sample_board: List[List[int]]) -> "Board": return

    def _next_turn(self) -> None: return

    @staticmethod
    def _valid_moves(board: Board, turn_count: int) -> Tuple[((int, int), (int, int))]: return

    @staticmethod
    def _valid_captures(board: Board, turn_count: int) -> Tuple[((int, int), (int, int))]: return
