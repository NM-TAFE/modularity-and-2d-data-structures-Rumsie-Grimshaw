from game_board import GameBoard
from game_manager import GameManager
from test import Test

manager = GameManager()
game_board = GameBoard()
test = Test()


# Main()
def main():
    start_game()


def start_game():
    game_board.generate_board()
    board_state = game_board.return_board_state()
    # test.testAddThreeNumbersToFirstThreeRows(game_board)
    game_completed = False

    while not game_completed:
        manager.display_board_state(board_state)
        empty_spaces = manager.return_count_empty_spaces(board_state)
        current_player = manager.get_player(empty_spaces)
        # test.testDisplayCurrentPlayer(current_player)
        player_move = manager.get_player_input(current_player)
        test.testReturnPlayerMove(f"Player move is: [{player_move}]")
        selected_space = game_board.return_board_index(player_move)
        is_empty_empty = manager.space_availability(board_state, selected_space)
        manager.alter_board_space(board_state, current_player, is_empty_empty, selected_space)
        board_state = game_board.return_board_state()


if __name__ == '__main__':
    main()
