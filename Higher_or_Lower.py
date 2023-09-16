import random

print("============MENU===========")
print("Welcome to Higher or Lower Game!")
print("Rules: \n You will enter the range of the number\n that you are going to guess. \n Guess the number, and if your guess \n is higher or lower\n It will determine it.")

while True:
    number_range = int(input("Enter number's range: "))
    number = random.randint(1, number_range)
    user_input = 0
    
    while user_input != number:
        user_input = int(input("Guess the number: "))
        if user_input > number:
            print("Lower")
        elif user_input < number:
            print("Higher")
        elif user_input == number:
            print(f"Correct! The number is: {number}")
            
    choice = input("Do you want to continue(Yes or No): ")
    if choice.lower() != "yes":
        print("Thank you for playing!")
        break
    else:
        continue