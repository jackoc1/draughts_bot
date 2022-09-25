import unittest

from draughts.board import Board, Piece, OccupiedError


class BoardTest(unittest.TestCase):
    """
    Tests mainly for 8 x 8 Boards for now. [row, column]

    I think I may actually have it setup such that I can't test if add piece adds to the private board attribute in
     the right place, only if add piece and get piece point to the same positions on the board...

    Did try to avoid any non-linear time operations since there are a lot of tests.
    """

    def setUp(self):
        self.board = Board(8, 8)

        self.populated_board = Board(8, 8)
        self.piece_position_1, self.piece_position_2, self.piece_position_3, self.piece_position_4 \
            = (2, 3), (6, 2), (1, 0), (7, 7)
        self.piece_colour_1, self.piece_colour_2, self.piece_colour_3, self.piece_colour_4 \
            = 0, 0, 1, 1

        self.populated_board.add_piece(self.piece_colour_1, self.piece_position_1)
        self.populated_board.add_piece(self.piece_colour_2, self.piece_position_2)
        self.populated_board.add_piece(self.piece_colour_3, self.piece_position_3)
        self.populated_board.add_piece(self.piece_colour_4, self.piece_position_4)
        self.populated_board.promote(self.piece_position_2)
        self.populated_board.promote(self.piece_position_4)

    def test_empty_squares_equal_zero(self):
        for row in range(self.board.num_rows):
            for col in range(self.board.num_cols):
                if self.board.get_piece((row, col)) != 0:
                    self.fail("Empty board does not consist of only zeroes.")

    def test_add_piece_adds_piece_to_correct_position(self):
        position_1, position_2, position_3 = (0, 0), (3, 4), (6, 3)
        self.board.add_piece(colour=0, position=position_1)
        self.board.add_piece(colour=0, position=position_2)
        self.board.add_piece(colour=0, position=position_3)

        self.assertIsInstance(self.board.get_piece(position_1), Piece)
        self.assertIsInstance(self.board.get_piece(position_2), Piece)
        self.assertIsInstance(self.board.get_piece(position_3), Piece)

    def test_add_piece_adds_piece_of_correct_colour(self):
        colour_1, colour_2 = 0, 1
        position_1, position_2 = (2, 3), (1, 6)
        test_piece_1 = Piece(colour=colour_1)
        test_piece_2 = Piece(colour=colour_2)
        self.board.add_piece(colour=colour_1, position=position_1)
        self.board.add_piece(colour=colour_2, position=position_2)

        self.assertEqual(test_piece_1, self.board.get_piece(position_1))
        self.assertEqual(test_piece_2, self.board.get_piece(position_2))

    def test_add_piece_does_not_add_any_other_pieces_to_any_other_positions(self):
        piece_position = (3, 3)
        self.board.add_piece(colour=0, position=piece_position)

        for row in range(self.board.num_rows):
            for col in range(self.board.num_cols):
                if (row, col) == piece_position:
                    continue
                if isinstance(self.board.get_piece((row, col)), Piece):
                    self.fail("add_piece added an extra piece.")

    def test_add_piece_does_not_add_promoted_pieces(self):
        piece_position_1, piece_position_2 = (7, 6), (2, 0)
        self.board.add_piece(colour=0, position=piece_position_1)
        self.board.add_piece(colour=1, position=piece_position_2)

        self.assertFalse(self.board.get_piece(piece_position_1).promoted)
        self.assertFalse(self.board.get_piece(piece_position_2).promoted)

    def test_remove_piece_removes_specified_piece(self):
        colour_1, colour_2 = 0, 1
        position_1, position_2 = (2, 3), (1, 6)
        self.board.add_piece(colour=colour_1, position=position_1)
        self.board.add_piece(colour=colour_2, position=position_2)
        self.board.remove_piece(position_1)
        self.board.remove_piece(position_2)

        self.assertEqual(0, self.board.get_piece(position_1))
        self.assertEqual(0, self.board.get_piece(position_2))

    def test_remove_piece_does_not_remove_any_other_pieces(self):
        remove_position = (5, 3)
        for row in range(self.board.num_rows):
            for col in range(self.board.num_cols):
                self.board.add_piece(colour=0, position=(row, col))
        self.board.remove_piece(remove_position)

        for row in range(self.board.num_rows):
            for col in range(self.board.num_cols):
                if (row, col) == remove_position:
                    continue
                if self.board.get_piece((row, col)) == 0:
                    self.fail("A piece besides the intended piece was removed.")

    def test_get_piece_returns_zero_for_unoccupied_squares(self):
        empty_position_1, empty_position_2 = (0, 4), (7, 7)
        self.assertEqual(0, self.board.get_piece(empty_position_1))
        self.assertEqual(0, self.board.get_piece(empty_position_2))

    def test_get_piece_returns_equivalent_piece_for_occupied_squares(self):
        piece_position_1, piece_position_2, piece_position_3, piece_position_4 = (1, 3), (5, 2), (6, 5), (7, 4)
        colour_1, colour_2, colour_3, colour_4 = 0, 0, 1, 1
        self.board.add_piece(colour_1, piece_position_1)
        self.board.add_piece(colour_2, piece_position_2)
        self.board.add_piece(colour_3, piece_position_3)
        self.board.add_piece(colour_4, piece_position_4)
        self.board.promote(piece_position_2)
        self.board.promote(piece_position_4)

        test_piece_1 = Piece(colour_1)
        test_piece_2 = Piece(colour_2)
        test_piece_3 = Piece(colour_3)
        test_piece_4 = Piece(colour_4)
        test_piece_2.promote()
        test_piece_4.promote()

        self.assertEqual(test_piece_1, self.board.get_piece(piece_position_1))
        self.assertEqual(test_piece_2, self.board.get_piece(piece_position_2))
        self.assertEqual(test_piece_3, self.board.get_piece(piece_position_3))
        self.assertEqual(test_piece_4, self.board.get_piece(piece_position_4))

    def test_get_player_pieces_does_not_return_any_of_the_other_players_pieces(self):
        player_1_pieces = self.populated_board.get_player_pieces(0)
        player_2_pieces = self.populated_board.get_player_pieces(1)

        for piece in player_1_pieces:
            if piece[0].colour != 0:
                self.fail("Player 2's pieces show up in player 1's pieces.")

        for piece in player_2_pieces:
            if piece[0].colour != 1:
                self.fail("Player 1's pieces show up in player 2's pieces.")

    def test_get_player_pieces_returns_all_that_players_pieces(self):
        """Player 2 pieces subtest reliant on player 1 pieces subtest being passed."""
        player_1_pieces = self.populated_board.get_player_pieces(0)
        player_2_pieces = self.populated_board.get_player_pieces(1)
        all_pieces = []
        for row in range(self.populated_board.num_rows):
            for col in range(self.populated_board.num_cols):
                if self.populated_board.get_piece((row, col)):
                    all_pieces.append([self.populated_board.get_piece((row, col)), (row, col)])

        for piece, position in player_1_pieces:
            all_pieces.remove([piece, position])
        for piece, _ in all_pieces:
            if piece.colour == 0:
                self.fail("Not all player 1 pieces in all pieces were found in player_1_pieces.")

        for piece, position in player_2_pieces:
            all_pieces.remove([piece, position])
        if all_pieces:
            self.fail("Not all player 2 pieces were found in player_2_pieces.")

    def test_get_player_pieces_returns_pieces_promoted_state_correctly(self):
        player_1_pieces = self.populated_board.get_player_pieces(0)
        player_2_pieces = self.populated_board.get_player_pieces(1)

        for piece, position in player_1_pieces:
            if piece != self.populated_board.get_piece(position):
                self.fail("Player 1's pieces do not match the pieces on the board.")

        for piece, position in player_2_pieces:
            if piece != self.populated_board.get_piece(position):
                self.fail("Player 2's pieces do not match the pieces on the board.")

    def test_get_player_returns_empty_list_for_players_with_no_pieces(self):
        self.assertEqual((), self.board.get_player_pieces(0))
        self.assertEqual((), self.board.get_player_pieces(1))

    def test_moved_piece_in_right_position(self):
        start_position_1 = (2, 0)
        end_position_1 = (3, 1)
        piece_1 = self.board.get_piece(start_position_1)
        self.board.move((start_position_1, end_position_1))

        start_position_2 = (5, 3)
        end_position_2 = (4, 4)
        piece_2 = self.board.get_piece(start_position_2)
        self.board.move((start_position_2, end_position_2))

        self.assertEqual(piece_1, self.board.get_piece(end_position_1))
        self.assertEqual(piece_2, self.board.get_piece(end_position_2))

    def test_moved_piece_previous_position_now_empty(self):
        start_position_1 = (2, 0)
        end_position_1 = (3, 1)
        self.board.move((start_position_1, end_position_1))

        start_position_2 = (5, 3)
        end_position_2 = (4, 4)
        self.board.move((start_position_2, end_position_2))

        self.assertEqual(0, self.board.get_piece(start_position_1))
        self.assertEqual(0, self.board.get_piece(start_position_2))

    def test_value_error_raised_if_invalid_start_position_passed_to_move(self):
        """4 start positions for the 4 edges of the board you can fall off."""
        start_position_1, end_position_1 = (-1, 2), (3, 2)
        start_position_2, end_position_2 = (9, 2), (3, 2)
        start_position_3, end_position_3 = (3, -2), (3, 2)
        start_position_4, end_position_4 = (3, 10), (3, 2)

        self.assertRaises(ValueError, self.board.move, (start_position_1, end_position_1))
        self.assertRaises(ValueError, self.board.move, (start_position_2, end_position_2))
        self.assertRaises(ValueError, self.board.move, (start_position_3, end_position_3))
        self.assertRaises(ValueError, self.board.move, (start_position_4, end_position_4))

    def test_value_error_raised_if_invalid_end_position_passed_to_move(self):
        """4 end positions for the 4 edges of the board you can fall off."""
        end_position_1, start_position_1 = (-1, 2), (3, 2)
        end_position_2, start_position_2 = (9, 2), (3, 2)
        end_position_3, start_position_3 = (3, -2), (3, 2)
        end_position_4, start_position_4 = (3, 10), (3, 2)

        self.assertRaises(ValueError, self.board.move, (start_position_1, end_position_1))
        self.assertRaises(ValueError, self.board.move, (start_position_2, end_position_2))
        self.assertRaises(ValueError, self.board.move, (start_position_3, end_position_3))
        self.assertRaises(ValueError, self.board.move, (start_position_4, end_position_4))

    def test_value_error_raised_if_invalid_start_and_end_position_passed_to_move(self):
        """4 start and end positions for the 4 edges of the board you can fall off. (Not exhaustive)"""
        start_position_1, end_position_1 = (-1, 2), (20, 3)
        start_position_2, end_position_2 = (9, 2), (3, 20)
        start_position_3, end_position_3 = (3, -2), (-2, 2)
        start_position_4, end_position_4 = (3, 10), (3, -6)

        self.assertRaises(ValueError, self.board.move, (start_position_1, end_position_1))
        self.assertRaises(ValueError, self.board.move, (start_position_2, end_position_2))
        self.assertRaises(ValueError, self.board.move, (start_position_3, end_position_3))
        self.assertRaises(ValueError, self.board.move, (start_position_4, end_position_4))

    def test_occupied_error_raised_if_end_position_of_move_occupied(self):
        self.board.add_piece(1, (7, 7))
        self.board.add_piece(1, (6, 6))
        invalid_move = ((7, 7), (6, 6))

        self.assertRaises(OccupiedError, self.board.move, invalid_move)

    def test_value_error_raised_if_invalid_position_passed_to_add_piece(self):
        """4 positions for the 4 edges of the board you can fall off."""
        position_1, position_2, position_3, position_4 = (-1, 3), (10, 4), (3, -2), (6, 9)

        self.assertRaises(ValueError, self.board.add_piece, (0, position_1))
        self.assertRaises(ValueError, self.board.add_piece, (0, position_2))
        self.assertRaises(ValueError, self.board.add_piece, (0, position_3))
        self.assertRaises(ValueError, self.board.add_piece, (0, position_4))

    def test_occupied_error_raised_if_position_passed_to_add_piece_is_already_occupied(self):
        position = (1, 1)
        self.board.add_piece(0, position)

        self.assertRaises(OccupiedError, self.board.add_piece, (0, position))

    def test_value_error_raised_if_invalid_position_passed_to_remove_piece(self):
        """4 positions for the 4 edges of the board you can fall off."""
        position_1, position_2, position_3, position_4 = (-1, 3), (10, 4), (3, -2), (6, 9)

        self.assertRaises(ValueError, self.board.remove_piece, position_1)
        self.assertRaises(ValueError, self.board.remove_piece, position_2)
        self.assertRaises(ValueError, self.board.remove_piece, position_3)
        self.assertRaises(ValueError, self.board.remove_piece, position_4)

    def test_value_error_raised_if_invalid_position_passed_to_get_piece(self):
        """4 positions for the 4 edges of the board you can fall off."""
        position_1, position_2, position_3, position_4 = (-1, 3), (10, 4), (3, -2), (6, 9)

        self.assertRaises(ValueError, self.board.get_piece, position_1)
        self.assertRaises(ValueError, self.board.get_piece, position_2)
        self.assertRaises(ValueError, self.board.get_piece, position_3)
        self.assertRaises(ValueError, self.board.get_piece, position_4)

    def test_value_error_raised_if_invalid_position_passed_to_promote(self):
        """4 positions for the 4 edges of the board you can fall off."""
        position_1, position_2, position_3, position_4 = (-1, 3), (10, 4), (3, -2), (6, 9)

        self.assertRaises(ValueError, self.board.promote, position_1)
        self.assertRaises(ValueError, self.board.promote, position_2)
        self.assertRaises(ValueError, self.board.promote, position_3)
        self.assertRaises(ValueError, self.board.promote, position_4)

    def test_value_error_raised_if_invalid_colour_passed_to_get_player_pieces(self):
        colour_less_than_zero = -1
        colour_greater_than_1 = 3
        colour_float_between_0_and_1 = 0.5
        colour_written_as_a_string = "black"

        self.assertRaises(ValueError, self.board.get_player_pieces, colour_less_than_zero)
        self.assertRaises(ValueError, self.board.get_player_pieces, colour_greater_than_1)
        self.assertRaises(ValueError, self.board.get_player_pieces, colour_float_between_0_and_1)
        self.assertRaises(ValueError, self.board.get_player_pieces, colour_written_as_a_string)

    def test_promote_promotes_the_specified_piece(self):
        promote_position_1, promote_position_2 = (5, 3), (7, 6)
        self.board.add_piece(0, promote_position_1)
        self.board.add_piece(1, promote_position_2)
        self.board.promote(promote_position_1)
        self.board.promote(promote_position_2)

        self.assertTrue(self.board.get_piece(promote_position_1).promoted)
        self.assertTrue(self.board.get_piece(promote_position_2).promoted)

    def test_promote_does_not_promote_any_other_pieces(self):
        promote_position = (5, 3)
        for row in range(self.board.num_rows):
            for col in range(self.board.num_cols):
                self.board.add_piece(colour=0, position=(row, col))
        self.board.promote(promote_position)

        for row in range(self.board.num_rows):
            for col in range(self.board.num_cols):
                if (row, col) == promote_position:
                    continue
                if self.board.get_piece((row, col)).promoted:
                    self.fail("A piece besides the intended piece was promoted.")

    def test_get_piece_returns_new_piece_object_each_call(self):
        piece_colour, piece_position = 0, (3, 4)
        self.board.add_piece(piece_colour, piece_position)
        test_piece_1, test_piece_2 = self.board.get_piece(piece_position), self.board.get_piece(piece_position)

        self.assertIsNot(test_piece_1, test_piece_2)

    def test_get_board_returns_new_board_object_each_call(self):
        test_board_1 = self.board.get_board()
        test_board_2 = self.board.get_board()

        self.assertIsNot(test_board_1, test_board_2)

    def test_get_player_pieces_returns_new_piece_objects_on_each_call(self):
        test_player_pieces_1 = self.populated_board.get_player_pieces(0)
        test_player_pieces_2 = self.populated_board.get_player_pieces(0)
        pieces_dict_1, pieces_dict_2 = dict(), dict()
        for piece, position in test_player_pieces_1:
            pieces_dict_1[position] = piece
        for piece, position in test_player_pieces_2:
            pieces_dict_2[position] = piece

        for position in pieces_dict_1.keys():
            if pieces_dict_1[position] is pieces_dict_2[position]:
                self.fail("Two different calls to get_player_pieces returned same piece")

    def test_promote_does_not_do_anything_to_board_if_used_on_empty_square(self):
        self.populated_board.promote((0, 7))

    def test_get_board_returns_a_board_equal_to_the_current_board(self):
        position_piece_1, position_piece_2, position_piece_3 = (2, 3), (6, 1), (0, 7)
        colour_piece_1, colour_piece_2, colour_piece_3 = 0, 0, 1
        self.board.add_piece(colour=colour_piece_1, position=position_piece_1)
        self.board.add_piece(colour=colour_piece_2, position=position_piece_2)
        self.board.add_piece(colour=colour_piece_3, position=position_piece_3)
        self.board.promote(position_piece_2)

        new_board = self.board.get_board()
        for row in range(self.board.num_rows):
            for col in range(self.board.num_cols):
                if self.board.get_piece((row, col)) != new_board.get_piece((row, col)):
                    self.fail("New Board not equal to current Board")


if __name__ == '__main__':
    unittest.main()
