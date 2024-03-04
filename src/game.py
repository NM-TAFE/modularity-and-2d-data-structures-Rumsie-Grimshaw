from board import game_board

# Check remaining spaces on board and assign player based on odd or even number of remaining empty spaces.
# Player One = Even and Player Two = Odd
def get_player():
    if game_board.board.count(game_board.empty) % 2 != 0:
        current_player = "X"
    else:
        current_player = "O"
    return current_player

def get_player_input(current_player):
    # prints a message denoting the current players turn and asks for user input
    while True:
        print("Next move for player " + current_player + " (0-8): ")
        player_input = input()
        if player_input.isdigit():
            if 0 <= int(player_input) <= 8 and game_board.board[int(player_input)] == game_board.empty:
                return player_input
            elif 0 <= int(player_input) <= 8 and game_board.board[int(player_input)] != game_board.empty:
                print("Space already taken!")
            else:
                print("Invalid input!")
        else:
            # display error message and repeat loop
            print("Invalid input!")


# Check if winning conditions met.
def is_winning_condition():
    game_board.is_win_condition_met()

# Begin the game
def start_game():
    while True:
        game_board.display_board()
        current_player = get_player()
        value = get_player_input(current_player)
        game_board.update_board(current_player, value)
        is_winning_condition()


if __name__ == '__main__':
    start_game()
