from typing import Tuple, List, Union

Position = Tuple[int, int]
Move = Tuple[Position, Position]


class Board:
    def __init__(self, num_rows: int = 8, num_cols: int = 8) -> None:
        self._board: Tuple[List[Union[int, Piece]], ...] = tuple([[0] * num_rows] * num_cols)
        self._num_rows = num_rows
        self._num_cols = num_cols

    num_rows = property(lambda self: self._num_rows)
    num_cols = property(lambda self: self._num_cols)

    def move(self, move: Move) -> None:
        piece = self.get_piece(move[0])
        self._board[move[0][0]][move[0][1]] = 0
        self._board[move[1][0]][move[1][1]] = piece

    def get_piece(self, position: Position) -> "Piece":
        """Returns new copy of piece"""
        piece = self._board[position[0]][position[1]]
        if piece:
            new_piece = Piece(piece.colour)
            if piece.promoted:
                new_piece.promote()
        else:
            new_piece = 0

        return new_piece

    def get_board(self) -> "Board":  # don't expose internals
        new_board = Board(self.num_rows, self.num_cols)
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                if piece := self.get_piece((row, col)):
                    new_board.add_piece(piece.colour, (row, col))
                    if piece.promoted:
                        new_board.promote((row, col))

        return new_board

    def get_player_pieces(self, colour: int) -> Tuple[Tuple["Piece", Position], ...]:
        player_pieces = []
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                piece = self.get_piece((row, col))
                if piece and piece.colour == colour:
                    player_pieces.append((piece, (row, col)))

        return tuple(player_pieces)

    def promote(self, position: Position) -> None:
        if self.get_piece(position):
            self._board[position[0]][position[1]].promote()

    def add_piece(self, colour: int, position: Position) -> None:
        if self.get_piece(position):
            raise OccupiedError

        self._board[position[0]][position[1]] = Piece(colour)

    def remove_piece(self, position: Position) -> None:
        self._board[position[0]][position[1]] = 0

    def __equal__(self, other: "Board") -> bool:
        equal = True
        if self.num_rows != other.num_rows:
            equal = False
        elif self.num_cols != other.num_cols:
            equal = False
        else:
            break_flag = False
            for row in range(self.num_rows):
                for col in range(self.num_cols):
                    if self.get_piece((row, col)) != other.get_piece((row, col)):
                        equal = False
                        break_flag = True
                        break
                if break_flag:
                    break

        return equal


class Piece:
    def __init__(self, colour: int) -> None:
        self._colour = colour
        self._promoted = False

    colour = property(lambda self: self._colour)
    promoted = property(lambda self: self._promoted)

    def promote(self) -> None:
        self._promoted = True

    def __eq__(self, other: "Piece") -> bool:
        return self._colour == other.colour and self._promoted == other.promoted


class OccupiedError(Exception):
    pass
