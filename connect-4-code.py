import os
import random

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# the main menu for the game
def print_board(board):
    clear_screen()
    print("========== Connect4 =========")
    print("Player 1: X       Player 2: O")
    print("\n", end="")
    print("  1   2   3   4   5   6   7")

    for row in board:
        print(" ---" * 7)
        for cell in row:
            if cell == 1:
                print("|", "X", "", end="")
            elif cell == 2:
                print("|", "O", "", end="")
            else:
                print("|   ", end="")
        print("|")

    print(" ---" * 7)
    print("=============================")

def is_winner(board, player):
    # Check for horizontal wins
    for row in board:
        for i in range(4):
            if all(cell == player for cell in row[i:i + 4]):
                return True

    # Check for vertical wins
    for col in range(7):
        for i in range(3):
            if all(board[i + j][col] == player for j in range(4)):
                return True

    # Check for diagonal wins (from bottom left to top right)
    for i in range(3):
        for j in range(4):
            if all(board[i + k][j + k] == player for k in range(4)):
                return True

    # Check for diagonal wins (from top left to bottom right)
    for i in range(3):
        for j in range(4):
            if all(board[i + 3 - k][j + k] == player for k in range(4)):
                return True

    return False

def is_board_full(board):
    return all(cell != 0 for row in board for cell in row)

def drop_piece(board, player, column):
    for i in range(5, -1, -1):
        if board[i][column - 1] == 0:
            board[i][column - 1] = player
            return True
    print("That column is full, please try again.")
    return False

def execute_player_turn(player, board):
    while True:
        user_input = validate_input("Player {}, please select a column (1-7): ".format(player), ["1", "2", "3", "4", "5", "6", "7"])
        move_valid = drop_piece(board, player, int(user_input))
        if move_valid:
            return int(user_input)

def cpu_player_easy(board, player):
    while True:
        vertical_move = random.randint(1, 7)
        executed_move_works = drop_piece(board, player, vertical_move)
        if executed_move_works:
            return vertical_move

def validate_input(prompt, valid_inputs):
    while True:
        user_input = input(prompt)
        if user_input in valid_inputs:
            return user_input
        else:
            print("Invalid input, please try again.")

def create_board():
    return [[0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0]]

def print_rules():
    print("================= Rules =================")
    print("Connect 4 is a two-player game where the")
    print("objective is to get four of your pieces")
    print("in a row either horizontally, vertically")
    print("or diagonally. The game is played on a")
    print("6x7 grid. The first player to get four")
    print("pieces in a row wins the game. If the")
    print("grid is filled and no player has won,")
    print("the game is a draw.")
    print("=========================================")

def local_2_player_game():
    board = create_board()
    player = 1

    while True:
        print_board(board)

        column = execute_player_turn(player, board)

        if is_winner(board, player):
            print_board(board)
            print("Player {} wins!".format(player))
            break

        if is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break

        player = 3 - player  # Switch player (1 to 2, 2 to 1)

def cpu_vs_player_game():
    board = create_board()
    player = 1

    while True:
        print_board(board)

        if player == 1:
            column = execute_player_turn(player, board)
        else:
            column = cpu_player_easy(board, player)

        if is_winner(board, player):
            print_board(board)
            if player == 1:
                print("Player {} wins!".format(player))
            else:
                print("CPU wins!")
            break

        if is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break

        player = 3 - player  # Switch player (1 to 2, 2 to 1)

def main():
    while True:
        clear_screen()

        print("=============== Main Menu ===============")
        print("Welcome to Connect 4!")
        print("1. View Rules")
        print("2. Play a local 2 player game")
        print("3. Play a game against the computer")
        print("4. Exit")
        print("=========================================")

        player_selection = validate_input("Please select an option (1, 2, 3, 4): ", ["1", "2", "3", "4"])

        if player_selection == "1":
            clear_screen()
            print_rules()
            validate_input("Please select 1 to return back to the main menu: ", ["1"])
        elif player_selection == "2":
            local_2_player_game()
            validate_input("Please select 1 to return back to the main menu: ", ["1"])
        elif player_selection == "3":
            cpu_vs_player_game()
            validate_input("Please select 1 to return back to the main menu: ", ["1"])
        else:
            clear_screen()

if __name__ == "__main__":
    main()
