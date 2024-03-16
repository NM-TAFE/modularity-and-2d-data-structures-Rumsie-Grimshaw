class GameBoard:
    def __init__(self):
        self.row = 3
        self.column = 3
        self.empty = " "
        self.board = []
        self.total_space = (self.row * self.column) - 1

    def __str__(self):
        return f"This is a game board!"

    def generate_board(self):
        for row in range(self.column):
            row = [self.empty] * self.row
            self.board.append(row)
        return self.board

    def return_board_state(self):
        return self.board

    def return_total_board_spaces(self):
        return self.total_space

    def return_board_index(self, player_input):
        index = 0
        count_x = 0
        count_y = 0

        for row in self.board:
            for spaces in range(0, len(row)):
                for space in range(0, len(row)):
                    # test.testDisplayIndex(index, count_x, count_y)
                    if count_x == len(row):
                        count_x = 0
                        count_y += 1

                    elif index == int(player_input):
                        board_space = count_y, count_x
                        return board_space

                    else:
                        count_x += 1
                        index += 1


if __name__ == '__main__':
    ...
