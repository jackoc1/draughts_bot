import unittest

from draughts.board import Move, Piece


class MoveTest(unittest.TestCase):
    def setUp(self):
        self.piece = Piece(0)

    def test_value_error_if_start_position_not_on_board(self):
        self.assertRaises(ValueError, Move.__init__, (self.piece, (-1, 0), (0, 1)))
        self.assertRaises(ValueError, Move.__init__, (self.piece, (8, 0), (9, 1)))

    def test_value_error_if_end_position_not_on_board(self):
        self.assertRaises(ValueError, Move.__init__, (self.piece, (0, 0), (-1, 1)))
        self.assertRaises(ValueError, Move.__init__, (self.piece, (7, 7), (8, 8)))

    def test_value_error_if_both_positions_not_on_board(self):
        self.assertRaises(ValueError, Move.__init__, (self.piece, (-1, -5), (0, -6)))
        self.assertRaises(ValueError, Move.__init__, (self.piece, (10, 10), (11, 11)))

    def test_value_error_if_start_position_not_on_dark_square(self):
        self.assertRaises(ValueError, Move.__init__, (self.piece, (0, 1), (1, 2)))
        self.assertRaises(ValueError, Move.__init__, (self.piece, (3, 0), (4, 1)))

    def test_value_error_if_unpromoted_piece_not_one_diagonal_forward(self):
        self.assertRaises(ValueError, Move.__init__, (self.piece, (0, 0), (0, 1)))
        self.assertRaises(ValueError, Move.__init__, (self.piece, (0, 0), (1, 0)))
        self.assertRaises(ValueError, Move.__init__, (self.piece, (0, 0), (5, 5)))
        self.assertRaises(ValueError, Move.__init__, (self.piece, (2, 2), (1, 1)))

    def test_value_error_if_promoted_piece_not_one_diagonal_forward_or_back(self):
        self.piece.promote()
        self.assertRaises(ValueError, Move.__init__, (self.piece, (0, 0), (1, 0)))
        self.assertRaises(ValueError, Move.__init__, (self.piece, (1, 1), (1, 2)))
        self.assertRaises(ValueError, Move.__init__, (self.piece, (2, 2), (0, 0)))
        self.assertRaises(ValueError, Move.__init__, (self.piece, (3, 5), (1, 7)))

    def test_no_errors_if_valid_move_unpromoted(self):
        try:
            Move(self.piece, (0, 0), (1, 1))
            Move(self.piece, (3, 5), (2, 6))
            Move(self.piece, (5, 5), (6, 6))
        except ValueError:
            self.fail("Valid move not accepted.")

    def test_no_errors_if_valid_move_promoted(self):
        self.piece.promote()
        try:
            Move(self.piece, (0, 0), (1, 1))
            Move(self.piece, (3, 5), (2, 4))
            Move(self.piece, (2, 2), (1, 3))
            Move(self.piece, (5, 5), (6, 4))
        except ValueError:
            self.fail("Valid move not accepted")


if __name__ == '__main__':
    unittest.main()
