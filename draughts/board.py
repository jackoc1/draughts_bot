from copy import deepcopy


class Board:
    def __init__(self):
        self._board = [[0] * 8] * 8

    def move(self, start_position, end_position):
        pass

    def capture(self, start_position, end_position):
        pass

    def get_board(self):  # don't expose internals
        pass

    def get_player_pieces(self, player):
        pass

    def get_piece(self, position):
        pass

    def _promote(self, piece):  # likely will delete
        pass

    def __deepcopy__(self, memodict={}):  # StackOverflow
        cls = self.__class__
        result = cls.__new__(cls)
        memodict[id(self)] = result
        for k, v in self.__dict__.items():
            setattr(result, k, deepcopy(v, memodict))
        return result


class Move:
    def __init__(self, piece, start_position, end_position):
        if 0 <= start_position < 8 and 0 <= end_position < 8:
            self._piece = piece
            self._start_position = start_position
            self._end_position = end_position
        else:
            raise ValueError(f"Invalid position ({self._start_position} {self._end_position}")

    piece = property(lambda self: self._piece)
    start_position = property(lambda self: self._start_position)
    end_position = property(lambda self: self._end_position)


class Capture:
    def __init__(self, piece, start_position, end_position):
        self._piece = piece
        self._start_position = start_position
        self._end_position = end_position

    piece = property(lambda self: self._piece)
    start_position = property(lambda self: self._start_position)
    end_position = property(lambda self: self._end_position)


class Piece:
    def __init__(self, player):
        self._player = player
        self._promoted = False

    player = property(lambda self: self._player)
    promoted = property(lambda self: self._promoted)

    def promote(self):
        pass

    def __eq__(self, other_piece):
        pass
