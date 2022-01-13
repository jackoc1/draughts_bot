import unittest
from typing import Tuple

from draughts.draughts import Draughts
from draughts.player import AbstractPlayer


class DraughtsTest(unittest.TestCase):
    """Unit tests for English draughts ruleset"""
    class TestPlayer(AbstractPlayer):
        def __init__(self, name): super(name)

        def get_move(self, start_position: Tuple[int, int], end_position: Tuple[int, int]) \
                -> Tuple[Tuple[int, int], Tuple[int, int]]:
            """Signature does not match base class so that I can return different moves in tests directly."""
            return start_position, end_position

        def accept_draw(self, accept: bool) -> bool:
            """Signature does not match base class so that I can return True/False directly."""
            return accept

        def move_accepted(self) -> None: super().move_accepted()

        def win(self) -> None: super().win()

    def setUp(self):
        player_1 = self.TestPlayer("Bob")
        player_2 = self.TestPlayer("Alice")
        self.game = Draughts(player_1, player_2)

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

    def test_there_are_no_pieces_on_non_starting_positions(self):
        pass


    def test_correct_valid_moves_offered_start_of_game_all_pieces_unpromoted(self):
        pass

    def test_valid_moves_player_1_piece_on_internal_square(self):
        pass

    def test_valid_moves_player_1_unpromoted_piece_on_edge_square(self):
        pass

    def test_valid_moves_player_1_piece_on_end_row_square(self):
        pass

    def test_square_not_in_valid_moves_if_already_occupied_player_1_unpromoted_piece(self):
        pass

    def test_normal_move_not_in_valid_moves_if_capture_available_player_1_unpromoted_piece(self):
        pass

    def test_player_1_can_not_capture_his_own_pieces_with_unpromoted_piece(self):
        pass

    def test_valid_moves_player_2_piece_on_edge_square(self):
        pass

    def test_valid_moves_player_2_piece_on_beginning_row_square(self):
        pass

    def test_square_not_in_valid_moves_if_already_occupied_player_2_unpromoted_piece(self):
        pass

    def test_normal_move_not_in_valid_moves_if_capture_available_player_2_unpromoted_piece(self):
        pass

    def test_player_2_can_not_capture_own_piece_with_unpromoted_piece(self):
        pass

    def test_valid_moves_promoted_player_1_piece_piece_on_internal_square(self):
        pass

    def test_valid_moves_promoted_player_1_piece_on_edge_square(self):
        pass

    def test_valid_moves_promoted_player_1_piece_on_end_square(self):
        pass

    def test_valid_moves_promoted_player_1_piece_piece_on_beginning_square(self):
        pass

    def test_player_1_can_not_capture_own_piece_with_promoted_piece(self):
        pass

    def test_normal_move_not_in_valid_moves_if_capture_available_player_1_promoted_piece(self):
        pass

    def test_valid_moves_promoted_player_2_piece_piece_on_internal_square(self):
        pass

    def test_valid_moves_one_promoted_player_2_piece_piece_on_end_square(self):
        pass

    def test_valid_moves_one_promoted_player_2_piece_piece_on_beginning_square(self):
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

    def test_turn_count_increments_end_of_turn(self):
        pass

    def test_player_1_unpromoted_piece_is_promoted_when_on_end_row_squares(self):
        pass

    def test_player_1_piece_does_not_promote_on_squares_other_than_end_row_squares(self):
        pass

    def test_player_2_unpromoted_piece_is_promoted_when_on_beginning_row_squares(self):
        pass

    def test_player_2_piece_does_not_promote_on_squares_other_than_beginning_row_squares(self):
        pass

    def test_player_1_forfeited(self):
        pass

    def test_player_2_forfeited(self):
        pass

    def test_player_1_offered_draw(self):
        pass

    def test_player_2_offered_draw(self):
        pass


if __name__ == '__main__':
    unittest.main()
