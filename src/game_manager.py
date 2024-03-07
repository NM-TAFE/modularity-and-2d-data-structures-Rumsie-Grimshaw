class GameManager:
    def __init__(self):
        ...

    def display_board_state(self, board_state):
        count = 0
        for row in board_state:
            print(board_state[count])
            count += 1

    def return_count_empty_spaces(self, board_state):
        count = 0
        for row in board_state:
            for space in row:
                if space == " ":
                    count += 1
        return count

    def get_player(self, empty_spaces):
        if empty_spaces % 2 != 0:
            return "X"
        else:
            return "0"

    def get_player_input(self, total_spaces, current_player):
        acceptable_range = False
        while not acceptable_range:
            print(f"Next move for player {current_player} (0-{total_spaces}): ")
            player_input = input()

            if player_input.isdigit() and 0 <= int(player_input) and int(player_input) <= total_spaces:
                return player_input
            else:
                print("Invalid input!")

    def space_availability(self, board_state, selected_space):
        count_y, count_x = selected_space
        if board_state[count_y][count_x] == " ":
            return True
        else:
            return False

    def alter_board_space(self, board_state, current_player, is_empty_space, selected_space):
        count_y, count_x = selected_space
        if not is_empty_space:
            print("Invalid input! Space is already taken!")
        else:
            board_state[count_y][count_x] = current_player

    def win_condition_met(self, board_state, current_player):
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
        count = 0
        for win in win_conditions:
            if win_conditions[count] != [current_player, current_player, current_player]:
                count += 1
            elif win_conditions[count] == [current_player, current_player, current_player]:
                print(f"Player {current_player} wins!")
                return True
            else:
                return False


if __name__ == '__main__':
    ...
