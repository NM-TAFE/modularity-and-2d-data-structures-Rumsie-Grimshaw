import unittest
from game_manager import GameManager
from game_board import GameBoard

class TestTicTacToe(unittest.TestCase):

    def setUp(self):
        # Set up objects
        self.game_board = GameBoard()
        self.game_manager = GameManager()

        # Test Game Preparation
        self.game_board.generate_board()
        self.board_state = self.game_board.return_board_state()

    # Check that values entered on a space that is already filled will not be overwritten. Test Index = 5
    def test_space_second_player_cannot_overwrite_first_player_space(self):
        # Arrange
        first_player = 'X'
        second_player = 'O'
        self.game_board.board[1][1] = first_player

        # Act
        self.game_manager.alter_board_space(self.board_state, second_player, False, (1, 1))
        result = self.game_board.board[1][1]

        # Assert
        self.assertEqual(result, first_player, "Space on board should still be occupied by player_one.")

    def test_game_is_not_yet_completed_with_both_players_having_three_turns_each(self):
        # Arrange
        first_player = 'X'
        self.board_state = [['X', ' ', 'X'],
                            [' ', 'O', 'X'],
                            ['O', ' ', 'O']]
        self.game_manager.display_board_state(self.board_state)
        empty_spaces = self.game_manager.return_count_empty_spaces(self.board_state)

        # Act
        result = self.game_manager.win_condition_met(self.board_state, first_player, empty_spaces)

        # Assert
        self.assertFalse(result, "No winner should be detected; and game should continue.")

    # Check that mock diagonal state is a successful win condition
    def test_game_results_in_a_draw(self):
        # Arrange
        current_player = 'X'
        self.board_state = [['X', 'O', 'X'],
                            ['O', 'O', 'X'],
                            ['O', 'X', 'O']]
        self.game_manager.display_board_state(self.board_state)
        empty_spaces = self.game_manager.return_count_empty_spaces(self.board_state)

        # Act
        win_condition = self.game_manager.win_condition_met(self.board_state, current_player, empty_spaces)
        result = win_condition

        # Assert
        self.assertTrue(result, "Game should result in a draw; rather than a win condition.")

    # Check that mock board state is a win via top row.
    def test_game_player_one_win_top_row(self):
        # Arrange
        current_player = 'X'
        self.board_state = [['X', 'X', 'X'],
                            ['O', 'O', ' '],
                            ['O', 'X', ' ']]
        self.game_manager.display_board_state(self.board_state)
        empty_spaces = self.game_manager.return_count_empty_spaces(self.board_state)

        # Act
        win_condition = self.game_manager.win_condition_met(self.board_state, current_player, empty_spaces)
        result = win_condition

        # Assert
        self.assertTrue(result, "Win message for 'X' should be displayed.")

    def test_game_player_two_wins_via_diagonal(self):
        # Arrange
        current_player = 'O'
        self.board_state = [['X', 'X', 'O'],
                            ['O', 'O', 'X'],
                            ['O', 'X', ' ']]
        self.game_manager.display_board_state(self.board_state)
        empty_spaces = self.game_manager.return_count_empty_spaces(self.board_state)

        # Act
        win_condition = self.game_manager.win_condition_met(self.board_state, current_player, empty_spaces)
        result = win_condition

        # Assert
        self.assertTrue(result, "Win message for 'O' should be displayed.")

    def test_current_player_is_player_one(self):
        # Arrange
        empty_spaces = self.game_manager.return_count_empty_spaces(self.board_state)
        current_player = self.game_manager.get_player(empty_spaces)

        # Act
        result = current_player

        # Assert
        self.assertEqual(result, 'X', "Should display 'X' as current_player")




