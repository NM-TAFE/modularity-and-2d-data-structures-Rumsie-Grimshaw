class GameBoard:
    def __init__(self):
        self.grid_x = 3
        self.grid_y = 3
        self.empty = " "
        self.board = []
        self.total_space = (self.grid_x * self.grid_y) - 1

    def __str__(self):
        return f"This is a game board!"

    def generate_board(self):
        for row in range(self.grid_y):
            row = [self.empty] * self.grid_x
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
            for spaces in row:
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
