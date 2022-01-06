import unittest

from draughts.board import Capture, Piece


class CaptureTest(unittest.TestCase):
    """
    Assumptions:
    """
    def setUp(self):
        self.piece = Piece(0)

    def test_value_error_if_end_position_not_on_board(self):
        self.assertRaises(ValueError, Capture.__init__, (self.piece, (7, 7), (9, 9)))
        self.assertRaises(ValueError, Capture.__init__, (self.piece, (0, 2), (-2, 4)))
        self.piece.promote()
        self.assertRaises(ValueError, Capture.__init__, (self.piece, (0, 0), (2, -2)))

    def test_value_error_if_unpromoted_piece_not_finishing_forward_two_squares_diagonally(self):
        self.assertRaises(ValueError, Capture.__init__, (self.plece, (3, 5), (1, 3)))
        self.assertRaises(ValueError, Capture.__init__, (self.piece, (4, 4), (7, 7)))
        self.assertRaises(ValueError, Capture.__init__, (self.piece, (5, 5), (7, 3)))
        self.assertRaises(ValueError, Capture.__init__, (self.piece, (3, 3), (3, 5)))

    def test_value_error_if_promoted_piece_not_finishing_two_squares_away_diagonally(self):
        self.piece.promote()
        self.assertRaises(ValueError, Capture.__init__, (self.piece, (1, 3), (4, 6)))
        self.assertRaises(ValueError, Capture.__init__, (self.piece, (2, 6), (4, 6)))
        self.assertRaises(ValueError, Capture.__init__, (self.piece, (5, 3), (3, 0)))

    def test_no_value_error_if_unpromoted_piece_makes_a_valid_capture_movement(self):
        try:
            Capture(self.piece, (5, 3), (3, 5))
            Capture(self.piece, (2, 4), (4, 6))
        except ValueError:
            self.fail("Value error raised despite valid capture arguments")

    def test_no_value_error_if_promoted_piece_makes_a_valid_capture_movement(self):
        self.piece.promote()
        try:
            Capture(self.piece, (6, 2), (4, 4))
            Capture(self.piece, (4, 4), (6, 2))
            Capture(self.piece, (5, 1), (3, 3))
            Capture(self.piece, (3, 3), (5, 1))
        except ValueError:
            self.fail("Value error raised despite valid capture arguments")

if __name__ == '__main__':
    unittest.main()
