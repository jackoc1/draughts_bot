import unittest

from draughts.board import Board, Piece, Move, Capture


class BoardTest(unittest.TestCase):
    def test_pieces_in_right_place_on_init(self):
        pass

    def test_pieces_assigned_to_the_right_players(self):
        pass

    def test_moved_piece_in_right_position(self):
        pass

    def test_moved_piece_previous_position_now_empty(self):
        pass

    def test_captured_piece_removed_from_board(self):
        pass

    def test_capturing_piece_in_right_position(self):
        pass

    def test_capturing_piece_previous_position_now_empty(self):
        pass

    def test_player_1_piece_promotes_when_last_row_reached(self):
        pass

    def test_player_2_piece_promotes_when_first_row_reached(self):
        pass

    def test_piece_does_not_promote_on_interior_rows(self):
        pass


if __name__ == '__main__':
    unittest.main()
