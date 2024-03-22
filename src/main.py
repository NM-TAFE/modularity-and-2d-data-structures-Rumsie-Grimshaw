from game_board import GameBoard
from game_manager import GameManager

game = GameManager()

# The function that begins the game and is called from if __name__ = '__main__'
def main():
    start_game()


# Game loop that runs until completion
def start_game():
    # Game loop starts here
    while not game.game_completed:
        game.get_player()
        player_move = game.get_player_input()
        selected_space = game.game_board.board_index(player_move)
        is_empty_empty = game.space_availability(selected_space)
        game.alter_board_space(is_empty_empty, selected_space)
        game.display_board_state()
        game.has_winner()
        game.is_draw()


if __name__ == '__main__':
    main()
