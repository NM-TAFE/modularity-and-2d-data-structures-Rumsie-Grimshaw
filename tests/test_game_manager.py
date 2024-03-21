import unittest
from game_manager import GameManager

class TestGameManager(unittest.TestCase):

    def setUp(self):
        # Set up objects
        self.game = GameManager()

    # Check that values entered on a space that is already filled will not be overwritten. Test Index = 5
    def test_space_second_player_cannot_overwrite_first_player_space(self):
        # Arrange
        self.game.game_board.board[1][1] = self.game.current_player

        # Act
        self.game.alter_board_space(False, (1, 1))
        result = self.game.game_board.board[1][1]

        # Assert
        self.assertEqual(result, self.game.first_player, "Space on board should still be occupied by player_one.")

    def test_game_is_not_yet_completed_with_both_players_having_three_turns_each(self):
        # Arrange
        self.game.game_board.board = [['X', ' ', 'X'],
                                      [' ', 'O', 'X'],
                                      ['O', ' ', 'O']]
        self.game.display_board_state()

        # Act
        result = self.game.has_winner()

        # Assert
        self.assertFalse(result, "No winner should be detected; and game should continue.")

    # Check that mock diagonal state is a successful win condition
    def test_game_results_in_a_draw(self):
        # Arrange
        self.current_player = self.game.current_player
        self.game.game_board.board = [['X', 'O', 'X'],
                                      ['X', 'O', 'X'],
                                      ['', 'X', 'O']]
        selected_space = self.game.game_board.board_index(6)
        self.game.alter_board_space(True, selected_space)

        # Act
        win_condition = self.game.has_winner()
        self.game.display_board_state()
        result = win_condition

        # Assert
        self.assertTrue(result, "Game should result in a draw; rather than a win condition.")

    # Check that mock board state is a win via top row.
    def test_game_player_one_win_top_row(self):
        # Arrange
        self.game.game_board.board = [['X', 'X', 'X'],
                                      ['O', 'O', ' '],
                                      ['O', 'X', ' ']]
        self.game.display_board_state()

        # Act
        win_condition = self.game.has_winner()
        result = win_condition

        # Assert
        self.assertTrue(result, "Win message for 'X' should be displayed.")

    def test_game_player_two_wins_via_diagonal(self):
        # Arrange
        self.game.game_board.board = [['X', 'X', 'O'],
                                      ['O', 'O', 'X'],
                                      ['O', 'X', ' ']]
        self.game.display_board_state()

        # Act
        win_condition = self.game.has_winner()
        result = win_condition

        # Assert
        self.assertTrue(result, "Win message for 'O' should be displayed.")

    def test_current_player_is_player_one(self):
        # Arrange
        self.game.game_board.board = [['X', 'X', 'O'],
                                      ['O', 'O', 'X'],
                                      ['O', 'X', ' ']]
        self.game.game_board.count_empty_spaces()

        # Act
        result = self.game.get_player()

        # Assert
        self.assertEqual(result, 'X', "Should display 'X' as current_player")
