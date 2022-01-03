class Piece:
    def __init__(self, player):
        self._player = player
        self._promoted = False

    colour = property(lambda self: self._colour)
    promoted = property(lambda self: self._promoted)

    def promote(self):
        pass
