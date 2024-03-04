class GameBoard:
    def __init__(self):
        self.empty = " "
        self.board = [self.empty] * 9

    def display_board(self):
        # Print the elements of the list (board[i]) index and insert string symbols to depict boarders
        print(self.board[0], "|", self.board[1], "|", self.board[2])
        print("---------")
        print(self.board[3], "|", self.board[4], "|", self.board[5])
        print("---------")
        print(self.board[6], "|", self.board[7], "|", self.board[8])
        print()

    def update_board(self, current_player, value):
        if self.board[int(value)] == self.empty:
            self.board[int(value)] = current_player
        return self

    def is_win_condition_met(self):
        win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]

        # Cross-reference index with win_conditions to determine if game is won.
        for index in win_conditions:
            if self.board[index[0]] == self.board[index[1]] == self.board[index[2]] != self.empty:
                self.display_board()
                print("Player", self.board[index[0]], "wins!")
                return True

        # Assess if the game state is a draw by evaluating empty spaces.
        if self.empty not in self.board:
            self.display_board()
            print("It's a tie!")
            return True

        return False


game_board = GameBoard()
