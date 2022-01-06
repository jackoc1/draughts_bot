import unittest

from draughts.board import Board, Piece, Move, Capture


class BoardTest(unittest.TestCase):
    def setUp(self):
        self.board = Board()

    def test_board_right_size(self):
        num_rows = len(self.board.get_board())
        num_cols = len(self.board.get_board()[0])
        self.assertEqual(num_rows, 8)
        self.assertEqual(num_cols, 8)

    def test_pieces_in_right_place_on_init(self):
        row_1 = [Piece(0), 0] * 4
        row_2 = [0, Piece(0)] * 4
        row_3 = [0] * 8
        row_4 = [0, Piece(1)] * 4
        row_5 = [Piece(1), 0] * 4
        test_board = [row_1, row_2, row_1, row_3, row_3, row_4, row_5, row_4]

        for row in range(len(test_board)):
            for col in range(len(test_board[0])):
                if self.board.get_piece((row, col)) != test_board[row][col]:
                    self.fail("Board did not initialize correctly.")

    def test_pieces_assigned_to_the_right_players(self):
        player_1_pieces = self.board.get_player_pieces(0)
        player_2_pieces = self.board.get_player_pieces(1)

        for position, piece in player_1_pieces:
            self.assertEqual(self.board.get_piece(position), piece)
            self.assertEqual(piece.player, 0)

        for position, piece in player_2_pieces:
            self.assertEqual(self.board.get_piece(position), piece)
            self.assertEqual(piece.player, 1)

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

    def test_captured_piece_removed_from_board(self):


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
