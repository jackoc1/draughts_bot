from typing import Tuple, Union
from draughts.board import Board
from draughts.player import AbstractPlayer

Position = Tuple[int, int]
Move = Tuple[Position, Position]


class Draughts:
    def __init__(self, player_1: AbstractPlayer, player_2: AbstractPlayer, board: Board = None,
                 auto_next_turn: bool = True) -> None:
        if board:
            self._board = board
        else:
            self._board = Draughts.create_standard_board()
        self._player_1: AbstractPlayer = player_1  # import different classes based on command line arguments
        self._player_2: AbstractPlayer = player_2
        self._turn_count: int = 0
        self._auto_next_turn: bool = auto_next_turn
        self._turn_draw_offered: int = None
        self._winner: AbstractPlayer = None  # Set to "draw" in case of draw, game is over when winner not None

    player_1 = property(lambda self: self._player_1)
    player_2 = property(lambda self: self._player_2)
    turn_count = property(lambda self: self._turn_count)
    turn_draw_offered = property(lambda self: self._turn_draw_offered)
    winner = property(lambda self: self._winner)

    def get_board(self) -> Board: return self._board.get_board()

    @staticmethod
    def valid_moves(board: Board, player: int) -> Tuple[Union[Move, str], ...]: return

    def next_turn(self) -> None: return  # do not increment when draw offered or multiple capture

    def start(self) -> None: return  # does turn 1 and first next turn starts turn 2

    @staticmethod
    def create_custom_board(sample_board: Tuple[Tuple[int, ...], ...]) -> Board:
        """
        sample_board must be a tuple based matrix with constant row and column size (> 0 each) where each element is
        filled with one of the following symbolic integers.

        0 - empty space
        1 - unpromoted player 1 piece
        2 - promoted player 1 piece
        3 - unpromoted player 2 piece
        4 - promoted player 2 piece

        :param sample_board: rows of digits representing the desired board.
        :return: a Board with the specified pieces in the specified positions.
        """
        return

    @staticmethod
    def create_standard_board() -> Board:
        return

    @staticmethod
    def _valid_moves(board: Board, player: int) -> Tuple[Move, ...]: return
    # flip board and apply player1 logic for player2 valid moves

    @staticmethod
    def _valid_captures(board: Board, player: int) -> Tuple[Move, ...]: return
