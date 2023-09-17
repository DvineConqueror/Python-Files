import random

def menu():
    print("============MENU===========")
    print("Welcome to Higher or Lower Game!")
    print("Rules: \n You will enter the range of the number\n that you are going to guess. \n Guess the number, and if your guess \n is higher or lower\n It will determine it.")
    print("============MENU===========")
    player_register()
    
def player_register():
    start = input("Do you want to start the game (Yes or No): ")
    if start.lower() != 'yes': 
        print("Ending the game!")
    else:
        register = input("Enter your name as Player: ")
        print(f"Player Name: {register}")
        main_game()

def main_game():
    
    high_score = 0
    
    while True:
        number_range = int(input("Enter number's range: "))
        number = random.randint(1, number_range)
        user_input = 0
        max_guesses = 5
        guesses = max_guesses

        while user_input != number and guesses > 0:
            user_input = int(input("Guess the number: "))
            if user_input > number:
                guesses -= 1
                print("Lower")
                print(f"Guesses left: {guesses}")
            elif user_input < number:
                guesses -= 1
                print("Higher")
                print(f"Guesses left: {guesses}")
            elif user_input == number:
                if guesses == max_guesses - 1:
                    points = 900
                else:
                    points = 900 - (max_guesses - guesses - 1) * 100
                print("You WON!")
                print(f"Correct! The number is: {number} and your guesses left is: {guesses}")
                print(f"Player: {player_register}")
                print(f"You scored {points} points!")

                if points > high_score:
                    high_score = points

                print(f"Player: {player_register}")
                print(f"Your High Score is: {high_score}")
                
        choice = input("Do you want to continue(Yes or No): ")
        if choice.lower() != "yes":
            print("Thank you for playing!")
            break
        else:
            continue
        

        
menu()