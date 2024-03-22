import unittest
from game_manager import GameManager

class TestGameManager(unittest.TestCase):

    def setUp(self):
        # Set up objects
        self.game = GameManager()

    # Check that values entered on a space that is already filled will not be overwritten. Test Index = 4
    def test_space_second_player_cannot_overwrite_first_player_space(self):
        # Arrange
        self.game.game_board.board[1][1] = self.game.current_player

        # Act
        self.game.game_board.get_board_index(4)
        self.game.alter_board_space()
        result = self.game.game_board.board[1][1]

        # Assert
        self.assertEqual(result, self.game.first_player, "Invalid Input message should be displayed.")

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
        self.game.game_board.board = [['X', 'O', 'X'],
                                      ['X', 'O', 'X'],
                                      [' ', 'X', 'O']]
        self.game.game_board.get_board_index(6)
        self.game.space_availability()
        self.game.alter_board_space()

        # Act
        result = self.game.is_draw
        self.game.display_board_state()

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
        result = self.game.win_by_row()

        # Assert
        self.assertTrue(result, "Win message for 'X' should be displayed.")

    def test_game_player_two_wins_via_diagonal(self):
        # Arrange
        self.game.game_board.board = [['X', 'X', 'O'],
                                      ['O', 'O', 'X'],
                                      ['O', 'X', ' ']]
        self.game.display_board_state()

        # Act
        result = self.game.win_by_descending_left_diagonal

        # Assert
        self.assertTrue(result)

    def test_player_two_wins_via_descending_left_diagonal(self):
        # Arrange
        self.game.game_board.board = [['X', 'X', 'O'],
                                      ['O', 'O', 'X'],
                                      ['O', 'X', ' ']]

        # Act
        result = self.game.win_by_descending_left_diagonal

        # Assert
        self.assertTrue(result, "Should display 'X' as current_player")

    def test_game_player_two_wins_via_top_down(self):
        # Arrange
        self.game.game_board.board = [['X', 'X', 'O'],
                                      ['O', 'X', 'O'],
                                      ['O', 'X', ' ']]
        self.game.display_board_state()

        # Act
        result = self.game.win_by_column()

        # Assert
        self.assertTrue(result, "Win message for 'O' should be displayed.")
