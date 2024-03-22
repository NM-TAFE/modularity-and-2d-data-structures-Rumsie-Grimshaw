"""
A TicTacToe GameBoard class that represents the game board and its state.
Date: 24.03.21
Author: Rhys Boyle
"""
class GameBoard:
    def __init__(self):
        self.row = 3
        self.column = 3
        self.empty = " "
        self.board = self.generate_board()
        self.total_space = self.row * self.column
        self.empty_spaces = self.count_empty_spaces()
        self.board_index = 0, 0

    def __str__(self):
        return f"This is a game board!"

    # Generates the object 2D data structure
    def generate_board(self):
        board = []
        for rows in range(self.column):
            row = [self.empty] * self.row
            board.append(row)
        return board

    # Returns a value that represents the amount of remaining empty board spaces
    def count_empty_spaces(self):
        count = 0
        for row in self.board:
            for space in row:
                if space == " ":
                    count += 1
        self.empty_spaces = count
        return self.empty_spaces

    # Iterate each index of row; increasing row # and resetting column count on each iteration until index found.
    # Return index when found.
    def get_board_index(self, player_move):
        # ToDo: This method could probably use rewriting.
        index = 0
        column = 0
        row = 0

        for rows in self.board:
            for spaces in range(0, len(rows)):
                for space in range(0, len(rows)):
                    if column == len(rows):
                        column = 0
                        row += 1

                    elif index == int(player_move):
                        self.board_index = row, column
                        return

                    else:
                        column += 1
                        index += 1


if __name__ == '__main__':
    ...
