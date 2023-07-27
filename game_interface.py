import sys
from main import print_menu, choose_option, play_game

def main():
    while True:
        print_menu()
        option = choose_option()
        if option == "exit":
            print("Good Game!")
            print("Exiting.....")
            sys.exit(0)
        else:
            play_game(option)

if __name__ == "__main__":
    main()
