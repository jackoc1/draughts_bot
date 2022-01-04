class Move:
    def __init__(self, start_position, end_position):
        if 0 <= start_position < 8 and 0 <= end_position < 8:
            self._start_position = start_position
            self._end_position = end_position
        else:
            raise ValueError(f"Invalid position ({self._start_position} {self._end_position}")

    start_position = property(lambda self: self._start_position)
    end_position = property(lambda self: self._end_position)
