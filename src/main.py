from game_board import GameBoard
from game_manager import GameManager
from test import Test

manager = GameManager()
game_board = GameBoard()
test = Test()


# The function that begins the game and is called from if __name__ = '__main__'
def main():
    start_game()


# Game loop that runs until completion
def start_game():
    # Initial Game Setup
    game_board.generate_board()
    board_state = game_board.return_board_state()
    manager.display_board_state(board_state)
    total_spaces = game_board.return_total_board_spaces()
    game_completed = False

    # Game loop starts here
    while not game_completed:
        empty_spaces = manager.return_count_empty_spaces(board_state)
        current_player = manager.get_player(empty_spaces)
        player_move = manager.get_player_input(total_spaces, current_player)
        selected_space = game_board.return_board_index(player_move)
        is_empty_empty = manager.space_availability(board_state, selected_space)
        manager.alter_board_space(board_state, current_player, is_empty_empty, selected_space)
        board_state = game_board.return_board_state()
        manager.display_board_state(board_state)
        win_condition = manager.win_condition_met(board_state, current_player)

        # Assessment of winning condition and pathways based on result
        if win_condition:
            game_completed = True
        if not win_condition:
            if empty_spaces - 1 == 0:
                print("Its a draw!")
                return
        else:
            continue


if __name__ == '__main__':
    main()
