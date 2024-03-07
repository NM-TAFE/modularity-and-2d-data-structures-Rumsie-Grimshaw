class GameManager():
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

    def get_player_input(self, current_player):
        acceptable_range = False
        while not acceptable_range:
            print(f"Next move for player {current_player} (0-8): ")
            player_input = input()

            if player_input.isdigit() and 0 <= int(player_input) and int(player_input) <= 8:
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


if __name__ == '__main__':
    ...
