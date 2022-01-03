from copy import deepcopy


class Board:
    def __init__(self):
        self._board = [[0] * 8] * 8

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

    def __deepcopy__(self, memodict={}):  # StackOverflow
        cls = self.__class__
        result = cls.__new__(cls)
        memodict[id(self)] = result
        for k, v in self.__dict__.items():
            setattr(result, k, deepcopy(v, memodict))
        return result
