# squares of the game board
empty = " "
# The game board represented as a list of 'empty' * by a number
board = [empty] * 9

def display_board():
    # Print the elements of the list (board[i]) index and insert string symbols to depict boarders
    print(board[0], "|", board[1], "|", board[2])
    print("---------")
    print(board[3], "|", board[4], "|", board[5])
    print("---------")
    print(board[6], "|", board[7], "|", board[8])
    print()

def is_win_condition_met():
    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]

    # Assess if game state is a draw by evaluating empty spaces.
    if empty not in board:
        print("It's a tie!")
        exit(0)
    else:
        # Cross-reference index with win_conditions to determine if game is won.
        for index in win_conditions:
            if board[index[0]] == board[index[1]] == board[index[2]] != empty:
                print("Player", board[index[0]], "wins!")
                exit(0)


