class GameBoard:
    def __init__(self):
        self.row = 3
        self.column = 3
        self.empty = " "
        self.board = []
        self.total_space = (self.row * self.column) - 1

    def __str__(self):
        return f"This is a game board!"

    # Generates the object 2D data structure
    def generate_board(self):
        for row in range(self.column):
            row = [self.empty] * self.row
            self.board.append(row)
        return self.board

    # Return the current state of the objects 2D data structure indexes
    def return_board_state(self):
        return self.board

    # Return a total count of the 2D data structure indexes
    def return_total_board_spaces(self):
        return self.total_space

    # Iterate each index of row; increasing row # and resetting column count on each iteration until index found.
    # Return index when found.
    def return_board_index(self, player_input):
        index = 0
        column = 0
        row = 0

        for rows in self.board:
            for spaces in range(0, len(rows)):
                for space in range(0, len(rows)):
                    if column == len(rows):
                        column = 0
                        row += 1

                    elif index == int(player_input):
                        board_space = row, column
                        return board_space

                    else:
                        column += 1
                        index += 1


if __name__ == '__main__':
    ...
