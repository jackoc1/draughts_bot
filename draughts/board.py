from typing import Tuple

from draughts.player import AbstractPlayer


class Board:
    def __init__(self, num_rows=8, num_cols=8) -> None:
        self._board = [[0] * num_rows] * num_cols
        self._num_rows = num_rows
        self._num_cols = num_cols

    num_rows = property(lambda self: self._num_rows)
    num_cols = property(lambda self: self._num_cols)

    def move(self, start_position: (int, int), end_position: (int, int)) -> None:
        pass

    def get_board(self) -> "Board":  # don't expose internals
        pass

    def get_player_pieces(self, player: AbstractPlayer) -> Tuple[("Piece", (int, int))]:
        pass

    def get_piece(self, position: (int, int)) -> "Piece":
        pass

    def promote(self, piece: "Piece") -> None:
        pass

    def add_piece(self, position: (int, int)) -> None:
        pass

    def remove_piece(self, position: (int, int)) -> None:
        pass


class Piece:
    def __init__(self, player: AbstractPlayer) -> None:
        self._player = player
        self._promoted = False

    player = property(lambda self: self._player)
    promoted = property(lambda self: self._promoted)

    def promote(self) -> None:
        pass

    def __eq__(self, other_piece: "Piece") -> bool:
        pass
