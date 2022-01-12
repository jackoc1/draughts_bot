import unittest

from draughts.board import Board, Piece


class BoardTest(unittest.TestCase):
    """
    Tests for 8 x 8 Boards only for now. [row, column]
    """
    def setUp(self):
        self.board = Board(8, 8)

    def test_add_piece_adds_correct_piece_to_correct_position(self):
        pass

    def test_add_piece_does_not_add_any_other_pieces_to_any_other_positions(self):
        pass

    def test_board_size_matches_parameters(self):
        board_1 = self.board
        board_2 = Board(10, 10)
        board_3 = Board(10, 8)
        self.assertEqual(self.board_1.num_rows, len(board_1.get_board()))
        self.assertEqual(self.board_1.num_cols, len(board_1.get_board()[0]))
        self.assertEqual(self.board_2.num_rows, len(board_2.get_board()))
        self.assertEqual(self.board_2.num_cols, len(board_2.get_board()[0]))
        self.assertEqual(self.board_3.num_rows, len(board_3.get_board()))
        self.assertEqual(self.board_3.num_cols, len(board_3.get_board()[0]))

    def test_remove_piece_removes_correct_piece(self):
        pass

    def test_remove_piece_does_not_remove_any_other_pieces(self):
        pass

    def test_moved_piece_in_right_position(self):
        start_position_1 = (2, 0)
        end_position_1 = (3, 1)
        piece_1 = self.board.get_piece(start_position_1)
        self.board.move(start_position_1, end_position_1)
        self.assertEqual(piece_1, self.board.get_piece(end_position_1))

        start_position_2 = (5, 3)
        end_position_2 = (4, 4)
        piece_2 = self.board.get_piece(start_position_2)
        self.board.move(start_position_2, end_position_2)
        self.assertEqual(piece_2, self.board.get_piece(end_position_2))

    def test_moved_piece_previous_position_now_empty(self):
        start_position_1 = (2, 0)
        end_position_1 = (3, 1)
        self.board.move(start_position_1, end_position_1)
        self.assertEqual(0, self.board.get_piece(start_position_1))

        start_position_2 = (5, 3)
        end_position_2 = (4, 4)
        self.board.move(start_position_2, end_position_2)
        self.assertEqual(0, self.board.get_piece(start_position_2))

    def test_value_error_raised_if_invalid_start_position_passed_to_move(self):
        pass

    def test_value_error_raised_if_invalid_end_position_passed_to_move(self):
        pass

    def test_value_error_raised_if_invalid_start_and_end_position_passed_to_move(self):
        pass

    def test_value_error_raised_if_invalid_position_passed_to_add_piece(self):
        pass

    def test_value_error_raised_if_invalid_position_passed_to_remove_piece(self):
        pass

    def test_value_error_raised_if_invalid_position_passed_to_get_piece(self):
        pass

    def test_promote_promotes_the_correct_piece(self):
        pass

    def test_promote_does_not_promote_any_other_pieces(self):
        pass

    def test_get_piece_does_not_return_reference_to_actual_piece_on_board(self):
        pass

    def test_get_board_does_not_return_reference_to_the_actual_board(self):
        pass

    def test_get_board_does_not_return_reference_to_any_actual_piece_on_the_board(self):
        pass

    def test_get_player_pieces_does_not_return_reference_to_any_actual_pieces_on_the_board(self):
        pass


if __name__ == '__main__':
    unittest.main()
