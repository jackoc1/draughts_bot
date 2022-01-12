from typing import Tuple, Type

from draughts.board import Board
from draughts.player import AbstractPlayer


class Draughts:
    def __init__(self, player_1: Type[AbstractPlayer], player_2: Type[AbstractPlayer]) -> None:
        self._board = Board()
        self._player_1 = player_1  # import different classes based on command line arguments
        self._player_2 = player_2
        self._turn_count = 0

    player_1 = property(lambda self: self._player_1)
    player_2 = property(lambda self: self._player_2)
    turn_count = property(lambda self: self._turn_count)

    def get_board(self) -> Board: return

    def new_game(self, swap_pieces: bool) -> None: return

    @staticmethod
    def valid_moves(board: Board) -> Tuple[Tuple[int, int], ...]: return

    @staticmethod
    def create_custom_board(sample_board: Tuple[Tuple[int, ...], ...]) -> Board: return

    def _next_turn(self) -> None: return

    @staticmethod
    def _valid_moves(board: Board, turn_count: int) -> Tuple[Tuple[int, int], ...]: return
    # flip board, increment turn_counter for player 2 valid moves

    @staticmethod
    def _valid_captures(board: Board, turn_count: int) -> Tuple[(int, int), ...]: return
