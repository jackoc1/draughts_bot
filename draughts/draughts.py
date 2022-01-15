from typing import Tuple
from draughts.board import Board
from draughts.player import AbstractPlayer


class Draughts:
    def __init__(self, player_1: AbstractPlayer, player_2: AbstractPlayer, board: Board = None) -> None:
        if board:
            self._board = board
        else:
            self._board = Draughts.create_standard_board()
        self._player_1 = player_1  # import different classes based on command line arguments
        self._player_2 = player_2
        self._turn_count = 0
        self._turn_draw_offered = None

    player_1 = property(lambda self: self._player_1)
    player_2 = property(lambda self: self._player_2)
    turn_count = property(lambda self: self._turn_count)

    def get_board(self) -> Board: return

    @staticmethod
    def valid_moves(board: Board, player: int) -> Tuple[Tuple[Tuple[int, int], Tuple[int, int]], ...]: return

    @staticmethod
    def create_custom_board(sample_board: Tuple[Tuple[int, ...], ...]) -> Board: return

    @staticmethod
    def create_standard_board() -> Board: return

    def _next_turn(self) -> None: return

    @staticmethod
    def _valid_moves(board: Board, player: int) -> Tuple[Tuple[int, int], ...]: return
    # flip board and apply player1 logic for player2 valid moves

    @staticmethod
    def _valid_captures(board: Board, player: int) -> Tuple[(int, int), ...]: return
