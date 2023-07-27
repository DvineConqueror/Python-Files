import random
import sys
import tkinter as tk
from tkinter import messagebox

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

# Other functions and game logic (same as before)

def main():
    global board, current_player, game_running, winner, game_mode

    print_menu()
    option = choose_option()

    if option == "human_vs_human":
        game_mode = "human_vs_human"
    elif option == "human_vs_bot":
        game_mode = "human_vs_bot"
    else:
        print("Exiting...")
        return

    root = tk.Tk()
    root.title("Tic Tac Toe")

    # Rest of the code (same as before)

if __name__ == "__main__":
    main()
