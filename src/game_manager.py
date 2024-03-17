class GameManager:
    def __init__(self):
        ...

    # Prints the board to screen
    def display_board_state(self, board_state):
        column_count = 0
        for row in board_state:
            string = " | ".join(row)
            print(string)
            if column_count < len(board_state) - 1:
                print("-" * len(string))
                column_count += 1

    # Returns a value that represents the amount of remaining empty board spaces
    def return_count_empty_spaces(self, board_state):
        count = 0
        for row in board_state:
            for space in row:
                if space == " ":
                    count += 1
        return count - 1

    # Sets the player based; determined by analysing if remaining spaces are odd or even.
    def get_player(self, empty_spaces):
        if empty_spaces % 2 != 0:
            return "O"
        else:
            return "X"

    # Ask player for input and validates input
    def get_player_input(self, total_spaces, current_player):
        acceptable_range = False
        while not acceptable_range:
            print(f"Next move for player {current_player} (0-{total_spaces}): ")
            player_input = input()

            # Checks that players input is both an int, and is less than the result of total_spaces;
            # else error.
            if player_input.isdigit() and 0 <= int(player_input) and int(player_input) <= total_spaces:
                return player_input
            else:
                print("Invalid input!")

    # Checks if space is empty and returns boolean value.
    def space_availability(self, board_state, selected_space):
        row, column = selected_space
        if board_state[row][column] == " ":
            return True
        else:
            return False

    # Stores player char in 2D data structure if array index is empty; else error.
    def alter_board_space(self, board_state, current_player, is_empty_space, selected_space):
        row, column = selected_space
        if not is_empty_space:
            print("Invalid input! Space is already taken!")
        else:
            board_state[row][column] = current_player

    # Determine if win conditions are met.
    def win_condition_met(self, board_state, current_player, empty_spaces):
        # TODO: Make modular!
        win_conditions = [
            # Left to Right
            [board_state[0][0], board_state[0][1], board_state[0][2]],
            [board_state[1][0], board_state[1][1], board_state[1][2]],
            [board_state[2][0], board_state[2][1], board_state[2][2]],
            # Top to Bottom
            [board_state[0][0], board_state[1][0], board_state[2][0]],
            # Diagonal Right
            [board_state[0][0], board_state[1][1], board_state[2][2]],
            # Diagonal Left
            [board_state[0][2], board_state[1][1], board_state[2][0]],
        ]
        for win in win_conditions:
            if win == [current_player, current_player, current_player]:
                print(f"Player {current_player} wins!")
                return True

        if empty_spaces == 0:
            print("Its a draw!")
            return True

        else:
            return False


if __name__ == '__main__':
    ...
