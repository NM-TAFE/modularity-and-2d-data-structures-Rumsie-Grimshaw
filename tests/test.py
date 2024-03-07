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


if __name__ == '__main__':
    ...
