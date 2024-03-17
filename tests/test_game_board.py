class Test:
    def __init__(self):
        ...

    def testAddThreeNumbersToFirstThreeRows(self, game_board):
        game_board.board[0][2] = '3'
        game_board.board[1][2] = '3'
        game_board.board[2][0] = '3'

    def testDisplayCurrentPlayer(self, current_player):
        print(f"Current Player is: {current_player}")

    def testReturnPlayerMove(self, player_move):
        print(player_move)

    def testDisplayIndex(self, index, count_x, count_y):
        print(f'index is: {index}   count_x is: {count_x}   count_y is: {count_y}')

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


if __name__ == '__main__':
    ...
