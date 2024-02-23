'''A monolithic and poorly written tic-tac-toe for you to refactor.'''
# Generated by ChatGPT 4
# Game state

# Players one and two
p1 = "X"
p2 = "O"
# squares of the game board
empty = " "
# The game board represented as a list of 'empty' * by a number
board = [empty] * 9

# Game loop
while True:
    # Print the elements of the list (board[i]) index and insert string symbols to depict boarders
    print(board[0], "|", board[1], "|", board[2])
    print("---------")
    print(board[3], "|", board[4], "|", board[5])
    print("---------")
    print(board[6], "|", board[7], "|", board[8])
    print()

    # Check for win
    # Identify the winning indexes of the list as hard coded values in sets of 3
    win_conditions = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]
    for wc in win_conditions:
        # checks the index of each of the sets of 3 for winning combinations
        if board[wc[0]] == board[wc[1]] == board[wc[2]] != empty:
            # Victory message
            print("Player", board[wc[0]], "wins!")
            exit(0)

    # Check for tie
    # if no more index in list == "empty" - game is draw
    if empty not in board:
        print("It's a tie!")
        exit(0)

    # Get next move
    while True:
        # Determine the player based on the count of 'empty' squares in board is odd or even
        # If odd set to player 1, else set to player two
        player = p1 if board.count(empty) % 2 == 1 else p2
        # prints a message denoting the current players turn and asks for user input
        move = input("Next move for player " + player + " (0-8): ")
        # checks if player input is int
        # checks if player input is between range of 0-8
        # checks if board[i] == "empty"
        if move.isdigit() and 0 <= int(move) <= 8 and board[int(move)] == empty:
            # overwrite index with player input and break to start loop from step one
            board[int(move)] = player
            break
        else:
            # display error message and repeat loop
            print("Invalid move, try again.")
