from typing import Tuple


class Board:
    def __init__(self, num_rows: int = 8, num_cols: int = 8) -> None:
        self._board = [[0] * num_rows] * num_cols
        self._num_rows = num_rows
        self._num_cols = num_cols

    num_rows = property(lambda self: self._num_rows)
    num_cols = property(lambda self: self._num_cols)

    def move(self, start_position: Tuple[int, int], end_position: Tuple[int, int]) -> None:
        pass

    def get_board(self) -> "Board":  # don't expose internals
        pass

    def get_player_pieces(self, colour: int) -> Tuple[Tuple["Piece", Tuple[int, int]], ...]:
        pass

    def get_piece(self, position: Tuple[int, int]) -> "Piece":
        pass

    def promote(self, position: Tuple[int, int]) -> None:
        pass

    def add_piece(self, colour: int, position: Tuple[int, int]) -> None:
        pass

    def remove_piece(self, position: Tuple[int, int]) -> None:
        pass

    def __equal__(self, other: "Board") -> bool:
        equal = True
        if self.num_rows != other.num_rows:
            equal = False
        elif self.num_cols != other.num_cols:
            equal = False
        else:
            for row in range(self.num_rows):
                for col in range(self.num_cols):
                    if self.get_piece((row, col)) != other.get_piece((row, col)):
                        equal = False
                        break
        return equal


class Piece:
    def __init__(self, colour: int) -> None:
        self._colour = colour
        self._promoted = False

    colour = property(lambda self: self._colour)
    promoted = property(lambda self: self._promoted)

    def promote(self) -> None:
        pass

    def __eq__(self, other_piece: "Piece") -> bool:
        pass
