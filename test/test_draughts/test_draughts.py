import unittest

from draughts.draughts import Draughts
from draughts.player_interface import PlayerInterface


class DraughtsTest(unittest.TestCase):
    class TestPlayer(PlayerInterface):
        def get_move(self, start_position, end_position):  # signatures not matching is fine, mock class only
            return start_position, end_position

        def forfeit(self):
            return "forfeit"

        def offer_draw(self):
            return "draw"

    def setUp(self):
        player_1 = self.TestPlayer()
        player_2 = self.TestPlayer()
        self.game = Draughts(player_1, player_2)

    def test_valid_moves_all_pieces_unpromoted(self):
        valid_moves_turn_one = []  # draw board and fill in
        self.assertCountEqual(self.game.valid_moves(0), valid_moves_turn_one)

    def test_valid_moves_there_are_promoted_pieces(self):
        pass

    def test_correct_player_prompted_for_move_on_each_turn(self):
        pass

    def test_same_player_prompted_to_move_again_if_another_capture_available(self):
        pass

    def test_turn_increments_end_of_turn(self):
        self.game.next_turn()

    def test_active_player_switches_end_of_turn(self):
        pass

    def test_player_forfeited(self):
        pass

    def test_player_offered_draw(self):
        pass


if __name__ == '__main__':
    unittest.main()
