import unittest
from game_manager import GameManager
from game_board import GameBoard

class TestGameManager(unittest.TestCase):

    def setUp(self):
        # Set up objects
        self.game_board = GameBoard()
        self.game_manager = GameManager()

        # Test Game Preparation
        self.game_board.generate_board()

    # Check that values entered on a space that is already filled will not be overwritten. Test Index = 5
    def test_space_second_player_cannot_overwrite_first_player_space(self):
        # Arrange
        self.game_board.board[1][1] = self.game_manager.first_player

        # Act
        self.game_manager.alter_board_space(self.game_board.board, self.game_manager.second_player, False, (1, 1))
        result = self.game_board.board[1][1]

        # Assert
        self.assertEqual(result, self.game_manager.first_player, "Space on board should still be occupied by player_one.")

    def test_game_is_not_yet_completed_with_both_players_having_three_turns_each(self):
        # Arrange
        first_player = 'X'
        self.game_board.board = [['X', ' ', 'X'],
                                 [' ', 'O', 'X'],
                                 ['O', ' ', 'O']]
        self.game_manager.display_board_state(self.game_board.board)

        # Act
        result = self.game_manager.win_condition_met(self.game_board.board, first_player,
                                                     self.game_board.empty_spaces)

        # Assert
        self.assertFalse(result, "No winner should be detected; and game should continue.")

    # Check that mock diagonal state is a successful win condition
    def test_game_results_in_a_draw(self):
        # Arrange
        current_player = 'X'
        self.game_board.board = [['X', 'O', 'X'],
                                 ['X', 'O', 'X'],
                                 ['O', 'X', 'O']]
        self.game_manager.display_board_state(self.game_board.board)
        self.game_board.count_empty_spaces()

        # Act
        win_condition = self.game_manager.win_condition_met(self.game_board.board, current_player,
                                                            self.game_board.empty_spaces)
        result = win_condition

        # Assert
        self.assertTrue(result, "Game should result in a draw; rather than a win condition.")

    # Check that mock board state is a win via top row.
    def test_game_player_one_win_top_row(self):
        # Arrange
        current_player = 'X'
        self.game_board.board = [['X', 'X', 'X'],
                                 ['O', 'O', ' '],
                                 ['O', 'X', ' ']]
        self.game_manager.display_board_state(self.game_board.board)

        # Act
        win_condition = self.game_manager.win_condition_met(self.game_board.board, current_player,
                                                            self.game_board.empty_spaces)
        result = win_condition

        # Assert
        self.assertTrue(result, "Win message for 'X' should be displayed.")

    def test_game_player_two_wins_via_diagonal(self):
        # Arrange
        current_player = 'O'
        self.game_board.board = [['X', 'X', 'O'],
                                 ['O', 'O', 'X'],
                                 ['O', 'X', ' ']]
        self.game_manager.display_board_state(self.game_board.board)

        # Act
        win_condition = self.game_manager.win_condition_met(self.game_board.board, current_player,
                                                            self.game_board.empty_spaces)
        result = win_condition

        # Assert
        self.assertTrue(result, "Win message for 'O' should be displayed.")

    def test_current_player_is_player_one(self):
        # Arrange
        empty_spaces = self.game_board.count_empty_spaces()
        current_player = self.game_manager.get_player(empty_spaces)

        # Act
        result = current_player

        # Assert
        self.assertEqual(result, 'X', "Should display 'X' as current_player")
