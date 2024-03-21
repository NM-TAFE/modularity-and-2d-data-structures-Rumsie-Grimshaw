from game_board import GameBoard
class GameManager:
    def __init__(self):
        self.game_board = GameBoard()
        self.first_player = 'X'
        self.second_player = 'O'
        self.current_player = self.get_player()

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

    # Ask player for input and validates input
    def get_player_input(self):
        acceptable_range = False
        while not acceptable_range:
            print(f"Next move for player {self.current_player} (0-{self.game_board.total_space - 1}): ")
            player_input = input()

            # Checks that players input is both an int, and is less than the result of total_spaces;
            # else error.
            if player_input.isdigit() and 0 <= int(player_input) and int(player_input) <= self.game_board.total_space - 1:
                return player_input
            else:
                print("Invalid input!")

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

    # Determine if win conditions are met.
    def has_winner(self):
        # TODO: Make modular!
        win_conditions = [
            # Left to Right
            [self.game_board.board[0][0], self.game_board.board[0][1], self.game_board.board[0][2]],
            [self.game_board.board[1][0], self.game_board.board[1][1], self.game_board.board[1][2]],
            [self.game_board.board[2][0], self.game_board.board[2][1], self.game_board.board[2][2]],
            # Top to Bottom
            [self.game_board.board[0][0], self.game_board.board[1][0], self.game_board.board[2][0]],
            # Diagonal Right
            [self.game_board.board[0][0], self.game_board.board[1][1], self.game_board.board[2][2]],
            # Diagonal Left
            [self.game_board.board[0][2], self.game_board.board[1][1], self.game_board.board[2][0]],
        ]
        for conditions in win_conditions:
            if all(self.current_player == player for player in conditions):
                print(f"Player {self.current_player} wins!")
                return True

        if self.game_board.empty_spaces <= 0:
            print("Its a draw!")
            return True

        return False


if __name__ == '__main__':
    ...
