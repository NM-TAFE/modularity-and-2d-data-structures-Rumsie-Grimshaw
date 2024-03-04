from board import game_board

# Check remaining spaces on board and assign player based on odd or even number of remaining empty spaces.
# Player One = Even and Player Two = Odd
def get_player():
    if game_board.board.count(game_board.empty) % 2 != 0:
        current_player = "X"
    else:
        current_player = "O"
    return current_player

def player_input(player):
    # prints a message denoting the current players turn and asks for user input
    player_move = input("Next move for player " + player + " (0-8): ")
    if player_move.isdigit():
        if 0 <= int(player_move) <= 8 and game_board.board[int(player_move)] == game_board.empty:
            game_board.board[int(player_move)] = player
        else:
            print("Invalid input, please enter a valid number between (0-8):")
    else:
        # display error message and repeat loop
        print("Invalid input, please enter a valid number between (0-8):")

# Check if winning conditions met.
def is_winning_condition():
    game_board.is_win_condition_met()

# Begin the game
def start_game():
    while True:
        game_board.display_board()
        player = get_player()
        player_input(player)
        is_winning_condition()


if __name__ == '__main__':
    start_game()
