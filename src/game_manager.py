from game_board import GameBoard
class GameManager:
    def __init__(self):
        self.game_board = GameBoard()
        self.first_player = 'X'
        self.second_player = 'O'
        self.current_player = self.get_player()
        self.game_completed = False
        self.display_board_state()

    # Prints the board to screen
    def display_board_state(self):
        column_count = 0
        for row in self.game_board.board:
            string = " | ".join(row)
            print(string)
            if column_count < len(self.game_board.board) - 1:
                print("-" * len(string))
                column_count += 1

    # Sets the player based; determined by analysing if remaining spaces are odd or even.
    def get_player(self):
        if self.game_board.empty_spaces % 2 != 0:
            self.current_player = self.first_player
        else:
            self.current_player = self.second_player
        return self.current_player

    # Ask player for input and validates player input
    def get_player_input(self):
        while True:
            print(f"Next move for player {self.current_player} (0-{self.game_board.total_space - 1}): ")
            player_input = input()
            # Checks that players input is both an int, and is within the acceptable range or throw ValueError.
            try:
                player_input = int(player_input)
                if 0 <= player_input < self.game_board.total_space:
                    return player_input
                else:
                    print("Input is out of range!")
            except ValueError:
                print("Invalid input! Please enter a valid integer.")

    # Checks if space is empty and returns boolean value.
    def space_availability(self, selected_space):
        row, column = selected_space
        if self.game_board.board[row][column] == " ":
            return True

    # Stores player char in 2D data structure if array index is empty; else error.
    def alter_board_space(self, is_empty_space, selected_space):
        row, column = selected_space
        if not is_empty_space:
            print("Invalid input! Space is already taken!")
        else:
            self.game_board.board[row][column] = self.current_player
            self.game_board.count_empty_spaces()

    # Iterate across all rows in board and return True if contains only current_players.
    def is_winner_by_row(self):
        for row in self.game_board.board:
            if all(self.current_player == player for player in row):
                return True

    # Iterate through each column in board and return True if each row[column] contains only current_player.
    def is_winner_by_column(self):
        for column in range(len(self.game_board.board[0])):
            if all(self.current_player == row[column] for row in self.game_board.board):
                return True

    # Retrieve the index of each row using the same int(index) value for [row][column] and return True if current_player
    # symbol stored in [0][0], [1][1], [2][2]
    def is_winner_by_descending_right_diagonal(self):
        row_length = len(self.game_board.board)
        if all(self.game_board.board[index][index] == self.current_player for index in range(row_length)):
            return True

    # Iterate the length of each row and check diagonally left if current player stored in [0][2], [1][1], [2][0].
    # Column index is calculated as the current row number - 1 to set direction.
    # Return True if all current_player stored in diagonal left spaces.
    def is_winner_by_descending_left_diagonal(self):
        row_length = len(self.game_board.board)
        modifier = -1
        if all(self.game_board.board[index][modifier-index] == self.current_player for index in range(row_length)):
            return True

    def is_draw(self):
        if self.game_board.empty_spaces == 0:
            print(f"Game is a draw!")
            self.game_completed = True

    # Determine if win conditions are met.
    def has_winner(self):
        is_winner_by_row = self.is_winner_by_row()
        is_winner_by_column = self.is_winner_by_column()
        is_winner_by_descending_left_diagonal = self.is_winner_by_descending_right_diagonal()
        is_winner_by_descending_right_diagonal = self.is_winner_by_descending_left_diagonal()

        conditions = [is_winner_by_row,
                      is_winner_by_column,
                      is_winner_by_descending_left_diagonal,
                      is_winner_by_descending_right_diagonal]

        for result in conditions:
            if result:
                print(f"Player {self.current_player} win!")
                self.game_completed = True


if __name__ == '__main__':
    ...
