import unittest

from draughts.board import Piece


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

    def test_equal_pieces_are_equal(self):
        piece_1 = Piece(0)
        test_piece_1 = Piece(0)
        piece_2 = Piece(1)
        test_piece_2 = Piece(1)
        piece_3 = Piece(0)
        piece_3.promote()
        test_piece_3 = Piece(0)
        test_piece_3.promote()

        self.assertEqual(piece_1, test_piece_1)
        self.assertEqual(piece_2, test_piece_2)
        self.assertEqual(piece_3, test_piece_3)

    def test_not_equal_pieces_are_not_equal(self):
        piece_1 = Piece(0)
        test_piece_1 = Piece(1)
        piece_2 = Piece(0)
        piece_2.promote()
        test_piece_2 = Piece(0)
        piece_3 = Piece(0)
        test_piece_3 = Piece(1)
        piece_3.promote()
        test_piece_3.promote()

        self.assertNotEqual(piece_1, test_piece_1)
        self.assertNotEqual(piece_2, test_piece_2)
        self.assertNotEqual(piece_3, test_piece_3)


if __name__ == '__main__':
    unittest.main()
