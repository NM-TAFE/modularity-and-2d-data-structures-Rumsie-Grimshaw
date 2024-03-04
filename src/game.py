import board

# Players one and two
player_one = "X"
player_two = "O"

# Check if winning conditions met.
def is_winning_condition():
    board.is_win_condition_met()

# Check remaining empty spaces on board and determine if odd or even number remains. Odd = player_one Even == player_two
def get_player():
    if board.board.count(board.empty) % 2 != 0:
        current_player = player_one
    else:
        current_player = player_two
    return current_player

def player_input():
    # prints a message denoting the current players turn and asks for user input
    player_move = input("Next move for player " + player + " (0-8): ")

    # Check is choice is an int, between 0 - 8 and that the space is empty. If so, fill space, else; request new number.
    while board.board[int(player_move)] == board.empty:
        if player_move.isdigit():
            if 0 <= int(player_move) <= 8:
                board.board[int(player_move)] = player
        else:
            # display error message and repeat loop
            print("Invalid move, try again.")


# Game loop
while True:
    board.display_board()
    player = get_player()
    player_input()
    is_winning_condition()
