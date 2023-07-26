import random
import sys


def print_menu():
    print("Welcome to Tic Tac Toe!")
    print("Please select an option:")
    print("1. Human vs Human")
    print("2. Human vs Bot")
    print("3. Exit")


def choose_option():
    while True:
        option = input("Enter your choice: ")
        if option == "1":
            return "human_vs_human"
        elif option == "2":
            return "human_vs_bot"
        elif option == "3":
            print("Good Game!")
            print("Exiting.....")
            sys.exit(0)
        else:
            print("Invalid choice. Please try again.")


def print_board(board):
    print(board[0] + "|" + board[1] + "|" + board[2])
    print("-----------")
    print(board[3] + "|" + board[4] + "|" + board[5])
    print("-----------")
    print(board[6] + "|" + board[7] + "|" + board[8])


def player_input(current_player, board):
    while True:
        inp = int(
            input(f"It is {current_player}'s turn! \nEnter a number from 1 - 9: "))
        if inp >= 1 and inp <= 9 and board[inp - 1] == " - ":
            board[inp - 1] = current_player
            break
        else:
            print("Invalid Choice, please select again.")
            print_board(board)


def check_horizontal(board, winner):
    if board[0] == board[1] == board[2] and board[0] != " - ":
        winner[0] = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != " - ":
        winner[0] = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != " - ":
        winner[0] = board[6]
        return True
    return False


def check_diagonal(board, winner):
    if board[0] == board[4] == board[8] and board[0] != " - ":
        winner[0] = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != " - ":
        winner[0] = board[2]
        return True
    return False


def check_vertical(board, winner):
    if board[0] == board[3] == board[6] and board[0] != " - ":
        winner[0] = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != " - ":
        winner[0] = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != " - ":
        winner[0] = board[2]
        return True
    return False


def check_win(board, winner):
    return check_diagonal(board, winner) or check_horizontal(board, winner) or check_vertical(board, winner)


def check_tie(board):
    return " - " not in board


def switch_player(current_player):
    return " O " if current_player == " X " else " X "


def computer_move(board):
    while True:
        position = random.randint(0, 8)
        if board[position] == " - ":
            board[position] = " O "
            break


def main():
    while True:
        print_menu()
        option = choose_option()

        if option == "human_vs_human":
            print("You have chosen to play Human vs Human.")
            board = [" - "] * 9
            current_player = " X "
            winner = [None]
            game_running = True

            while game_running:
                print_board(board)
                player_input(current_player, board)

                if check_win(board, winner) or check_tie(board):
                    game_running = False
                else:
                    current_player = switch_player(current_player)

            print_board(board)

            if winner[0]:
                print(f"The winner is {winner[0]}!")
            else:
                print("It's a tie!")

        elif option == "human_vs_bot":
            print("You have chosen to play Human vs Bot.")
            board = [" - "] * 9
            current_player = " X "
            winner = [None]
            game_running = True

            while game_running:
                print_board(board)

                if current_player == " X ":
                    player_input(current_player, board)
                else:
                    computer_move(board)

                if check_win(board, winner) or check_tie(board):
                    game_running = False
                else:
                    current_player = switch_player(current_player)

            print_board(board)

            if winner[0]:
                if winner[0] == " X ":
                    print("Congratulations! You won!")
                else:
                    print("The bot wins!")
            else:
                print("It's a tie!")

        else:
            print("Exiting...")
            break


if __name__ == "__main__":
    main()
