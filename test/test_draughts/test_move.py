import unittest

from draughts.board import Move, Piece


class MoveTest(unittest.TestCase):
    """
    Assumptions:
    """
    def setUp(self):
        self.piece = Piece(0)

    def test_value_error_if_start_position_not_on_board(self):
        self.assertRaises(ValueError, Move.__init__, (self.piece, (0, -1), (1, 0)))
        self.assertRaises(ValueError, Move.__init__, (self.piece, (0, 8), (1, 9)))

    def test_value_error_if_end_position_not_on_board(self):
        self.assertRaises(ValueError, Move.__init__, (self.piece, (0, 0), (1, -1)))
        self.assertRaises(ValueError, Move.__init__, (self.piece, (7, 7), (8, 8)))

    def test_value_error_if_both_positions_not_on_board(self):
        self.assertRaises(ValueError, Move.__init__, (self.piece, (-5, -1), (-6, 0)))
        self.assertRaises(ValueError, Move.__init__, (self.piece, (10, 10), (11, 11)))

    def test_value_error_if_start_position_not_on_dark_square(self):
        self.assertRaises(ValueError, Move.__init__, (self.piece, (1, 0), (2, 1)))
        self.assertRaises(ValueError, Move.__init__, (self.piece, (0, 3), (1, 4)))

    def test_value_error_if_unpromoted_piece_not_one_diagonal_forward(self):
        self.assertRaises(ValueError, Move.__init__, (self.piece, (0, 0), (1, 0)))
        self.assertRaises(ValueError, Move.__init__, (self.piece, (0, 0), (0, 1)))
        self.assertRaises(ValueError, Move.__init__, (self.piece, (0, 0), (5, 5)))
        self.assertRaises(ValueError, Move.__init__, (self.piece, (2, 2), (1, 1)))

    def test_value_error_if_promoted_piece_not_one_diagonal_forward_or_back(self):
        self.piece.promote()
        self.assertRaises(ValueError, Move.__init__, (self.piece, (0, 0), (0, 1)))
        self.assertRaises(ValueError, Move.__init__, (self.piece, (1, 1), (2, 1)))
        self.assertRaises(ValueError, Move.__init__, (self.piece, (2, 2), (0, 0)))
        self.assertRaises(ValueError, Move.__init__, (self.piece, (5, 3), (7, 1)))

    def test_no_value_errors_if_valid_move_unpromoted(self):
        try:
            Move(self.piece, (0, 0), (1, 1))
            Move(self.piece, (5, 3), (6, 2))
            Move(self.piece, (5, 5), (6, 6))
        except ValueError:
            self.fail("Value error raised despite valid move arguments.")

    def test_no_value_errors_if_valid_move_promoted(self):
        self.piece.promote()
        try:
            Move(self.piece, (0, 0), (1, 1))
            Move(self.piece, (5, 3), (4, 2))
            Move(self.piece, (2, 2), (3, 1))
            Move(self.piece, (5, 5), (4, 6))
        except ValueError:
            self.fail("Value error raised despite valid move arguments.")


if __name__ == '__main__':
    unittest.main()
