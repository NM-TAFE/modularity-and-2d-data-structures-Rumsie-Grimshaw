import unittest
from game_board import GameBoard
class TestGameBoard(unittest.TestCase):
    def setUp(self):
        # Set up objects
        self.game_board = GameBoard()
        self.game_board.generate_board()

    def test_board_columns_per_row_equal_to_three_by_default(self):
        # Arrange
        result = self.game_board.column

        # Assert
        self.assertEqual(result, 3, "Default board column count should = 3.")

    def test_board_row_count_equal_to_three_by_default(self):
        # Arrange
        result = self.game_board.row

        # Assert
        self.assertEqual(result, 3, "Default board row count should = 3.")

    def test_return_total_empty_spaces_of_board(self):
        # Act
        self.game_board.total_space = self.game_board.row * self.game_board.column

        # Assert
        self.assertEqual(self.game_board.total_space, 9, "Default board should contain 9 spaces as is a 3x3 grid.")

    def test_alter_board_size_and_return_total_spaces_of_board(self):
        # Arrange
        self.game_board.row = 5
        self.game_board.column = 5

        # Act
        total_spaces = self.game_board.row * self.game_board.column

        # Assert
        self.assertEqual(total_spaces, 25, "Altered board should contain 25 spaces as is a 5x5 grid.")

    def test_return_the_correct_index_of_board_based_on_player_input(self):
        # Arrange
        player_input = 5

        # Act
        result = self.game_board.board_index(player_input)

        # Assert
        self.assertEqual(result, (1, 2), "Return game_board.board[1][2] on a standard 3x3 board")


if __name__ == '__main__':
    ...
