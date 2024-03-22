from game_board import GameBoard
from game_manager import GameManager

game = GameManager()

# The function that begins the game and is called from if __name__ = '__main__'
def main():
    start_game()


# Game loop that runs until completion
def start_game():
    # Game loop starts here
    game.display_board_state()
    while not game.game_completed:
        game.get_player()
        game.get_player_input()
        game.game_board.get_board_index(game.player_move)
        game.space_availability()
        game.alter_board_space()
        game.display_board_state()
        game.has_winner()
        game.is_draw()


if __name__ == '__main__':
    main()
