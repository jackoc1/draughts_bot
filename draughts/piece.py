class Piece:
    def __init__(self, player):
        self._player = player
        self._promoted = False

    player = property(lambda self: self._player)
    promoted = property(lambda self: self._promoted)

    def promote(self):
        pass
