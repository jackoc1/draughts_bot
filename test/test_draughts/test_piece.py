import unittest
from draughts.piece import Piece


class PieceTest(unittest.TestCase):
    def test_no_playerless_instantiation(self):
        self.assertRaises(Exception, Piece.__init__, ())

    def test_player_must_be_0_or_1(self):
        Piece(0)
        Piece(1)
        self.assertRaises(Exception, Piece.__init__, 2)
        self.assertRaises(Exception, Piece.__init__, "dark")

    def test_default_promoted_status_false(self):
        piece = Piece(0)
        self.assertEqual(piece.promoted, False)

    def test_promote_unpromoted_piece(self):
        piece = Piece(1)
        self.assertEqual(piece.promoted, False)
        piece.promote()
        self.assertEqual(piece.promoted, True)

    def test_promote_promoted_piece(self):
        piece = Piece(0)
        self.assertEqual(piece.promoted, False)
        piece.promote()
        self.assertEqual(piece.promoted, True)
        piece.promoted()
        self.assertEqual(piece.promoted, True)


if __name__ == '__main__':
    unittest.main()
