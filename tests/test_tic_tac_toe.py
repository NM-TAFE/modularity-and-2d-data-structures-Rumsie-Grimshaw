import unittest

import game
from board import GameBoard

class TestTicTacToe(unittest.TestCase):

    def setUp(self):
        self.game_board = GameBoard()

    # Check value entered by player is appended to correct board space
    def test_input_is_correct(self):

        # Arrange
        current_player = 'X'
        value = 7

        # Act
        self.game_board.update_board(current_player, value)
        self.game_board.display_board()

        # Assert
        self.assertEqual(self.game_board.board[int(value)], current_player)

    # Check that values entered on a space that is already filled will not be overwritten. Test Index = 5
    def test_space_already_taken(self):

        # Arrange
        first_player = '0'
        second_player = 'X'
        index = 5

        # Act
        self.game_board.update_board(first_player, value=index)
        self.game_board.update_board(second_player, value=index)
        result = self.game_board.board[index]
        self.game_board.display_board()

        # Assert
        self.assertEqual(result, first_player)