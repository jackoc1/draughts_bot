import unittest
from typing import Tuple, List

from draughts.draughts import Draughts
from draughts.player import AbstractPlayer
from draughts.board import Board


class MockPlayer(AbstractPlayer):
    """
    Feeling somewhat clever trying to come up with a mock player despite not actually looking very far into mocking
    practices. move_stack to be able to have player 1 and 2 play against each other just using API calls feels good.
    """
    def __init__(self, name: str, move_queue: List[Tuple[Tuple[int, int], Tuple[int, int]], ...] = None,
                 accept: bool = None):
        super(name)
        self.move_queue = move_queue
        self.accept = accept

    def get_move(self, valid_moves: Tuple[Tuple[Tuple[int, int], Tuple[int, int]], ...]) \
            -> Tuple[Tuple[int, int], Tuple[int, int]]:
        return self.move_queue.pop(0)

    def accept_draw(self) -> bool:
        return self.accept

    def move_accepted(self) -> None: return

    def win(self) -> None: return

    def draw(self) -> None: return


class DraughtsTest(unittest.TestCase):
    """Unit tests for English draughts ruleset"""
    def setUp(self):
        self.player_1 = MockPlayer("Bob")
        self.player_2 = MockPlayer("Alice")
        self.game = Draughts(self.player_1, self.player_2, auto_next_turn=False)

        self.player_3 = MockPlayer("John")
        self.player_4 = MockPlayer("Henrique")
        sample_board = ((0, 0, 0, 2, 0, 4, 0, 0),
                        (3, 0, 3, 0, 4, 0, 4, 0),
                        (0, 0, 0, 3, 0, 3, 0, 0),
                        (0, 0, 2, 0, 0, 0, 0, 0),
                        (0, 3, 0, 0, 0, 1, 0, 0),
                        (0, 0, 0, 0, 4, 0, 2, 0),
                        (0, 0, 0, 1, 0, 1, 0, 0),
                        (1, 0, 0, 0, 4, 0, 0, 0))
        complex_board = Draughts.create_custom_board(sample_board=sample_board)
        self.complex_game = Draughts(self.player_3, self.player_4, complex_board, auto_next_turn=False)

        self.empty_board = Board()

    def test_pieces_in_right_place_on_default_init_8_by_8_standard_board(self):
        player_1_piece_positions = ((0, 0), (0, 2), (0, 4), (0, 6),
                                    (1, 1), (1, 3), (1, 5), (1, 7),
                                    (2, 0), (2, 2), (2, 4), (2, 6))
        player_2_piece_positions = ((5, 1), (5, 3), (5, 5), (5, 7),
                                    (6, 0), (6, 2), (6, 4), (6, 6),
                                    (7, 1), (7, 3), (7, 5), (7, 7))
        board = self.game.get_board()

        for position in player_1_piece_positions:
            piece = board.get_piece(position)
            if piece.colour != 0 and not piece.promoted:
                self.fail("Player 1 did not have the required pieces in the required positions.")

        for position in player_2_piece_positions:
            piece = board.get_piece(position)
            if piece.colour != 1 and not piece.promoted:
                self.fail("Player 2 did not have the required pieces in the required positions.")

    def test_pieces_in_right_place_and_right_attributes_on_custom_board(self):
        position_player_promoted = (((0, 0), 0, False), ((0, 4), 1, True), ((1, 3), 0, False), ((1, 5), 0, False),
                                    ((2, 4), 1, True), ((2, 6), 0, True), ((3, 1), 1, False), ((3, 5), 0, False),
                                    ((4, 2), 0, True), ((5, 3), 1, False), ((5, 5), 1, False), ((6, 0), 1, False),
                                    ((6, 2), 1, False), ((6, 4), 1, True), ((6, 6), 1, True), ((7, 3), 0, True),
                                    ((7, 5), 1, True))
        custom_board = self.complex_game.get_board()

        for ppp in position_player_promoted:
            piece = custom_board.get_piece(ppp[0])
            if piece.colour != ppp[1] or piece.promoted != ppp[2]:
                self.fail("The pieces on the custom board do not match the sample board.")

    def test_no_pieces_in_what_are_supposed_to_be_empty_squares_on_custom_board(self):
        position_player_promoted = (((0, 0), 0, False), ((0, 4), 1, True), ((1, 3), 0, False), ((1, 5), 0, False),
                                    ((2, 4), 1, True), ((2, 6), 0, True), ((3, 1), 1, False), ((3, 5), 0, False),
                                    ((4, 2), 0, True), ((5, 3), 1, False), ((5, 5), 1, False), ((6, 0), 1, False),
                                    ((6, 2), 1, False), ((6, 4), 1, True), ((6, 6), 1, True), ((7, 3), 0, True),
                                    ((7, 5), 1, True))
        positions = [ppp[0] for ppp in position_player_promoted]
        custom_board = self.complex_game.get_board()

        for row in range(custom_board.num_rows):
            for col in range(custom_board.num_cols):
                if (row, col) in positions:
                    continue
                if custom_board.get_piece((row, col)) != 0:
                    self.fail("There was an unspecified piece placed on the board.")

    def test_pieces_are_in_right_place_from_create_standard_board(self):
        player_1_piece_positions = ((0, 0), (0, 2), (0, 4), (0, 6),
                                    (1, 1), (1, 3), (1, 5), (1, 7),
                                    (2, 0), (2, 2), (2, 4), (2, 6))
        player_2_piece_positions = ((5, 1), (5, 3), (5, 5), (5, 7),
                                    (6, 0), (6, 2), (6, 4), (6, 6),
                                    (7, 1), (7, 3), (7, 5), (7, 7))
        board = self.game.create_standard_board()

        for position in player_1_piece_positions:
            piece = board.get_piece(position)
            if piece.colour != 0 and not piece.promoted:
                self.fail("Player 1 did not have the required pieces in the required positions.")

        for position in player_2_piece_positions:
            piece = board.get_piece(position)
            if piece.colour != 1 and not piece.promoted:
                self.fail("Player 2 did not have the required pieces in the required positions.")

    def test_there_are_no_pieces_on_non_starting_positions_8_by_8_standard_board(self):
        player_1_piece_positions = ((0, 0), (0, 2), (0, 4), (0, 6),
                                    (1, 1), (1, 3), (1, 5), (1, 7),
                                    (2, 0), (2, 2), (2, 4), (2, 6))
        player_2_piece_positions = ((5, 1), (5, 3), (5, 5), (5, 7),
                                    (6, 0), (6, 2), (6, 4), (6, 6),
                                    (7, 1), (7, 3), (7, 5), (7, 7))
        starting_positions = player_1_piece_positions + player_2_piece_positions
        board = self.game.get_board()

        for row in range(board.num_rows):
            for col in range(board.num_cols):
                if (row, col) not in starting_positions:
                    if board.get_piece((row, col)) != 0:
                        self.fail("There was a piece on a non-starting square.")

    def test_valid_moves_only_returns_move_with_a_player_piece_on_the_starting_square_turn_one_game_state(self):
        """Could strengthen by moving pieces around board a bit."""
        board = self.game.get_board()

        for move in Draughts.valid_moves(board, 0):
            starting_position = move[0]
            if board.get_piece(starting_position) == 0:
                self.fail("Valid moves returned an impossible move")

    def test_valid_moves_only_returns_move_with_a_player_piece_on_the_starting_square_complex_game_state(self):
        """Could strengthen by moving pieces around board a bit."""
        complex_board = self.complex_game.get_board()

        for move in Draughts.valid_moves(complex_board, 0):
            starting_position = move[0]
            if complex_board.get_piece(starting_position) == 0:
                self.fail("Valid moves returned an impossible move")

    def test_valid_moves_only_returns_moves_with_a_piece_on_the_starting_square_of_the_move_turn_one_game_state(self):
        """Could strengthen by moving pieces around board a bit."""
        board = self.game.get_board()

        for move in Draughts.valid_moves(board, 0):
            starting_position = move[0]
            if board.get_piece(starting_position) == 0:
                self.fail("Valid moves returned an impossible move")

    def test_valid_moves_only_returns_moves_with_a_piece_on_the_starting_square_of_the_move_complex_game_state(self):
        """Could strengthen by moving pieces around board a bit."""
        complex_board = self.complex_game.get_board()

        for move in Draughts.valid_moves(complex_board, 0):
            starting_position = move[0]
            if complex_board.get_piece(starting_position) == 0:
                self.fail("Valid moves returned an impossible move")

    def test_valid_moves_only_returns_moves_with_ending_square_empty_turn_one_game_state(self):
        pass

    def test_valid_moves_player_1_only_returns_moves_for_player_1_turn_one_game_state(self):
        """Could strengthen by moving pieces around board a bit."""
        board = self.game.get_board()

        for move in Draughts.valid_moves(board, 0):
            starting_position = move[0]
            if board.get_piece(starting_position).colour != 0:
                self.fail("Valid moves player 1 returned a move for a piece they do not own.")

    def test_valid_moves_player_2_only_returns_moves_for_player_2_turn_one_game_state(self):
        """Could strengthen by moving pieces around board a bit."""
        board = self.game.get_board()

        for move in Draughts.valid_moves(board, 1):
            starting_position = move[0]
            if board.get_piece(starting_position).colour != 1:
                self.fail("Valid moves player 2 returned a move for a piece they do not own.")

    def test_correct_valid_moves_offered_to_player_1_start_of_game(self):
        board = self.game.get_board()
        test_valid_moves = (((2, 0), (3, 1)), ((2, 2), (3, 1)), ((2, 2), (3, 3)), ((2, 4), (3, 3)),
                            ((2, 4), (3, 5)), ((2, 6), (3, 5)), ((2, 6), (3, 7)))
        test_valid_moves = sorted(test_valid_moves)
        valid_moves = Draughts.valid_moves(board, 0)
        valid_moves = sorted(valid_moves)

        self.assertEqual(valid_moves, test_valid_moves)

    def test_correct_valid_moves_offered_to_player_2_start_of_game(self):
        board = self.game.get_board()
        test_valid_moves = (((5, 1), (4, 0)), ((5, 1), (4, 2)), ((5, 3), (4, 2)), ((5, 3), (4, 4)),
                            ((5, 5), (4, 4)), ((5, 5), (4, 6)), ((5, 7), (4, 6)))
        test_valid_moves = sorted(test_valid_moves)
        valid_moves = Draughts.valid_moves(board, 1)
        valid_moves = sorted(valid_moves)

        self.assertEqual(valid_moves, test_valid_moves)

    def test_valid_moves_player_1_unpromoted_piece_on_internal_square_both_diagonals_free(self):
        test_board = Board()
        test_board.add_piece(0, (1, 1))
        test_valid_moves = sorted((((1, 1), (2, 0)), ((1, 1), (2, 3))))
        valid_moves = sorted(Draughts.valid_moves(test_board, 0))

        self.assertEqual(test_valid_moves, valid_moves)

    def test_valid_moves_player_1_unpromoted_player_1_piece_on_internal_square_one_diagonal_free(self):
        """Test the two invalid moves aren't returned. Can assume rest works as other tests cover."""
        test_board = Board()
        test_board.add_piece(0, (1, 1))
        test_board.add_piece(0, (2, 0))
        test_board.add_piece(0, (4, 4))
        test_board.add_piece(0, (5, 5))
        invalid_moves = (((1, 1), (2, 0)), ((4, 4), (5, 5)))
        valid_moves = Draughts.valid_moves(test_board, 0)

        self.assertNotIn(invalid_moves[0], valid_moves)
        self.assertNotIn(invalid_moves[1], valid_moves)

    def test_valid_moves_player_1_unpromoted_piece_on_internal_square_no_diagonals_free(self):
        """Test the two invalid moves aren't returned. Can assume rest works as other tests cover."""
        test_board = Board()
        test_board.add_piece(0, (1, 1))
        test_board.add_piece(0, (2, 0))
        test_board.add_piece(0, (4, 4))
        test_board.add_piece(0, (5, 5))
        invalid_moves = (((1, 1), (2, 0)), ((4, 4), (5, 5)))
        valid_moves = Draughts.valid_moves(test_board, 0)

        self.assertNotIn(invalid_moves[0], valid_moves)
        self.assertNotIn(invalid_moves[1], valid_moves)

    def test_valid_moves_player_1_unpromoted_piece_on_edge_square_only_diagonal_free(self):
        pass

    def test_valid_moves_player_1_unpromoted_piece_on_edge_square_only_diagonal_blocked(self):
        pass

    def test_normal_move_not_in_valid_moves_if_capture_available_player_1_unpromoted_piece(self):
        pass

    def test_player_1_can_not_capture_his_own_pieces_with_unpromoted_piece(self):
        pass

    def test_valid_moves_player_2_unpromoted_piece_on_internal_square_both_diagonals_free(self):
        pass

    def test_valid_moves_player_2_unpromoted_piece_on_internal_square_one_diagonal_free(self):
        pass

    def test_valid_moves_player_2_unpromoted_piece_on_internal_square_no_diagonals_free(self):
        pass

    def test_valid_moves_player_2_unpromoted_piece_on_edge_square_only_diagonal_free(self):
        pass

    def test_valid_moves_player_2_unpromoted_piece_on_edge_square_only_diagonal_blocked(self):
        pass

    def test_normal_move_not_in_valid_moves_if_capture_available_player_2_unpromoted_piece(self):
        pass

    def test_player_2_can_not_capture_own_piece_with_unpromoted_piece(self):
        pass

    def test_valid_moves_promoted_player_1_piece_on_internal_square(self):
        pass

    def test_valid_moves_promoted_player_1_piece_on_edge_square(self):
        pass

    def test_valid_moves_promoted_player_1_piece_on_end_square(self):
        pass

    def test_valid_moves_promoted_player_1_piece_on_beginning_square(self):
        pass

    def test_player_1_can_not_capture_own_piece_with_promoted_piece(self):
        pass

    def test_normal_move_not_in_valid_moves_if_capture_available_player_1_promoted_piece(self):
        pass

    def test_valid_moves_promoted_player_2_piece_on_internal_square(self):
        pass

    def test_valid_moves_one_promoted_player_2piece_on_end_square(self):
        pass

    def test_valid_moves_one_promoted_player_2_piece_on_beginning_square(self):
        pass

    def test_player_2_can_not_capture_own_piece_with_promoted_piece(self):
        pass

    def test_normal_move_not_in_valid_moves_if_capture_available_player_2_promoted_piece(self):
        pass

    def test_only_player_1_to_move_on_odd_turns(self):
        pass

    def test_only_player_2_to_move_on_even_turns(self):
        pass

    def test_player_1_capture_piece_removed_from_board(self):
        pass

    def test_player_2_captured_piece_removed_from_board(self):
        pass

    def test_player_1_prompted_to_move_again_if_another_capture_available(self):
        pass

    def test_player_2_prompted_to_move_again_if_another_capture_available(self):
        pass

    def test_if_prompted_to_move_again_turn_count_does_not_increment(self):
        pass

    def test_player_1_unpromoted_piece_is_promoted_when_on_end_row(self):
        sample_board = ((0, 0, 0, 0, 0, 0, 0, 4),
                        (1, 0, 0, 0, 0, 0, 0, 0),
                        (0, 0, 0, 0, 0, 0, 0, 0),
                        (0, 0, 0, 0, 0, 0, 0, 0),
                        (0, 0, 0, 0, 0, 0, 0, 0),
                        (0, 0, 0, 0, 0, 0, 0, 0),
                        (0, 0, 0, 0, 0, 0, 0, 0),
                        (0, 0, 0, 0, 0, 0, 0, 0))
        custom_board = Draughts.create_custom_board(sample_board)
        player_1_move_queue = [((6, 0), (7, 1))]
        player_2_move_queue = [((7, 7), (6, 6)), ((6, 6), (7, 7))]
        player_1 = MockPlayer("One", player_1_move_queue)
        player_2 = MockPlayer("Two", player_2_move_queue)
        game = Draughts(player_1, player_2, board=custom_board, auto_next_turn=False)
        game.next_turn()

        piece = game.get_board().get_piece((7, 1))
        self.assertTrue(piece.promoted)

    def test_player_1_piece_does_not_promote_on_rows_other_than_end_row(self):
        sample_board = ((0, 0, 0, 0, 0, 0, 0, 4),
                        (0, 0, 0, 0, 0, 0, 0, 0),
                        (0, 0, 0, 0, 0, 0, 0, 0),
                        (0, 0, 0, 0, 0, 0, 0, 0),
                        (0, 0, 0, 0, 0, 0, 0, 0),
                        (0, 0, 0, 0, 0, 0, 0, 0),
                        (0, 0, 0, 0, 0, 0, 0, 0),
                        (1, 0, 0, 0, 0, 0, 0, 0))
        custom_board = Draughts.create_custom_board(sample_board)
        player_1_move_queue = [((0, 0), (1, 1)), ((1, 1), (2, 0)), ((2, 0), (3, 1)), ((3, 1), (4, 0)),
                               ((4, 0), (5, 1)), ((5, 1), (6, 0))]
        player_2_move_queue = [((7, 7), (6, 6)), ((6, 6), (7, 7))] * 10
        player_1 = MockPlayer("One", player_1_move_queue)
        player_2 = MockPlayer("Two", player_2_move_queue)
        game = Draughts(player_1, player_2, board=custom_board, auto_next_turn=False)
        while player_1.move_queue:
            game.next_turn()

        piece = game.get_board().get_piece((6, 0))
        self.assertFalse(piece.promoted)

    def test_player_2_unpromoted_piece_is_promoted_when_on_beginning_row(self):
        sample_board = ((0, 0, 0, 0, 0, 0, 0, 0),
                        (0, 0, 0, 0, 0, 0, 0, 0),
                        (0, 0, 0, 0, 0, 0, 0, 0),
                        (0, 0, 0, 0, 0, 0, 0, 0),
                        (0, 0, 0, 0, 0, 0, 0, 0),
                        (0, 0, 0, 0, 0, 0, 0, 0),
                        (0, 0, 0, 0, 0, 0, 0, 3),
                        (2, 0, 0, 0, 0, 0, 0, 0))
        custom_board = Draughts.create_custom_board(sample_board)
        player_1_move_queue = [((0, 0), (1, 1))]
        player_2_move_queue = [((1, 7), (0, 6))]
        player_1 = MockPlayer("One", player_1_move_queue)
        player_2 = MockPlayer("Two", player_2_move_queue)
        game = Draughts(player_1, player_2, board=custom_board, auto_next_turn=False)
        game.next_turn()
        game.next_turn()

        piece = game.get_board().get_piece((0, 6))
        self.assertTrue(piece.promoted)

    def test_player_2_piece_does_not_promote_on_rows_other_than_beginning_row(self):
        sample_board = ((0, 0, 0, 0, 0, 0, 0, 3),
                        (0, 0, 0, 0, 0, 0, 0, 0),
                        (0, 0, 0, 0, 0, 0, 0, 0),
                        (0, 0, 0, 0, 0, 0, 0, 0),
                        (0, 0, 0, 0, 0, 0, 0, 0),
                        (0, 0, 0, 0, 0, 0, 0, 0),
                        (0, 0, 0, 0, 0, 0, 0, 0),
                        (2, 0, 0, 0, 0, 0, 0, 0))
        custom_board = Draughts.create_custom_board(sample_board)
        player_1_move_queue = [((0, 0), (1, 1)), ((1, 1), (0, 0))] * 10
        player_2_move_queue = [((7, 7), (6, 6)), ((6, 6), (5, 7)), ((5, 7), (4, 6)),
                               ((4, 6), (3, 7)), ((3, 7), (2, 6)), ((2, 6), (1, 7))]
        player_1 = MockPlayer("One", player_1_move_queue)
        player_2 = MockPlayer("Two", player_2_move_queue)
        game = Draughts(player_1, player_2, board=custom_board, auto_next_turn=False)
        while player_2.move_queue:
            game.next_turn()

        piece = game.get_board().get_piece((1, 7))
        self.assertFalse(piece.promoted)

    def test_player_1_forfeited_sets_winner_to_player_2(self):
        self.player_1.move_queue = ["forfeit"]
        self.game.start()

        self.assertIs(self.game.winner, self.player_2)

    def test_player_2_forfeited_sets_winner_to_player_1(self):
        self.player_1.move_queue = [((2, 0), (3, 1))]
        self.player_2.move_queue = ["forfeit"]
        self.game.start()
        self.game.next_turn()

        self.assertIs(self.game.winner, self.player_2)

    def test_player_1_offered_draw_sets_turn_draw_offered_to_current_turn_count(self):
        self.player_1.move_queue = ["draw", ((2, 0), (3, 1))]
        self.player_2.accept = False
        self.game.start()

        self.assertEqual(self.game.turn_draw_offered, 1)

    def test_player_2_offered_draw_sets_turn_draw_offered_to_current_turn_count(self):
        self.player_1.move_queue = [((2, 0), (3, 1))]
        self.player_1.accept = False
        self.player_2.move_queue = ["draw", ((5, 7), (4, 6))]
        self.game.start()
        self.game.next_turn()

        self.assertEqual(self.game.turn_draw_offered, 2)

    def test_game_ends_forty_turns_after_turn_draw_offered_auto_turn_true(self):
        sample_board = ((0, 0, 0, 0, 0, 0, 0, 4),
                        (0, 0, 0, 0, 0, 0, 0, 0),
                        (0, 0, 0, 0, 0, 0, 0, 0),
                        (0, 0, 0, 0, 0, 0, 0, 0),
                        (0, 0, 0, 0, 0, 0, 0, 0),
                        (0, 0, 0, 0, 0, 0, 0, 0),
                        (0, 0, 0, 0, 0, 0, 0, 0),
                        (2, 0, 0, 0, 0, 0, 0, 0))
        board = Draughts.create_custom_board(sample_board)
        player_1_move_queue = [((0, 0), (1, 1)), ((1, 1), (0, 0))] + ["draw"] + \
                              [((0, 0), (1, 1)), ((1, 1), (0, 0))] * 30
        player_2_move_queue = [((7, 7), (6, 6)), ((6, 6), (7, 7))] * 30
        player_1 = MockPlayer("Ricardo Milos", player_1_move_queue, False)
        player_2 = MockPlayer("Rick Bugez", player_2_move_queue, True)
        game = Draughts(player_1, player_2, board=board)
        game.start()
        end_turn_count = game.turn_count

        self.assertEqual(end_turn_count, 44)

    def test_game_ends_forty_turns_after_turn_draw_offered_auto_turn_false(self):
        sample_board = ((0, 0, 0, 0, 0, 0, 0, 4),
                        (0, 0, 0, 0, 0, 0, 0, 0),
                        (0, 0, 0, 0, 0, 0, 0, 0),
                        (0, 0, 0, 0, 0, 0, 0, 0),
                        (0, 0, 0, 0, 0, 0, 0, 0),
                        (0, 0, 0, 0, 0, 0, 0, 0),
                        (0, 0, 0, 0, 0, 0, 0, 0),
                        (2, 0, 0, 0, 0, 0, 0, 0))
        board = Draughts.create_custom_board(sample_board)
        player_1_move_queue = [((0, 0), (1, 1)), ((1, 1), (0, 0))] + ["draw"] + \
                              [((0, 0), (1, 1)), ((1, 1), (0, 0))] * 30
        player_2_move_queue = [((7, 7), (6, 6)), ((6, 6), (7, 7))] * 30
        player_1 = MockPlayer("Ricardo Milos", player_1_move_queue, False)
        player_2 = MockPlayer("Rick Bugez", player_2_move_queue, True)
        game = Draughts(player_1, player_2, board=board)
        lagged_turn_count = 0
        game.start()
        while lagged_turn_count != game.turn_count:
            lagged_turn_count += 1
            game.next_turn()
        end_turn_count = game.turn_count

        self.assertEqual(end_turn_count, 44)


if __name__ == '__main__':
    unittest.main()
