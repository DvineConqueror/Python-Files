# SIMPLE CALCULATOR BY DOMINIC

print("Dominic's Simple Calculator!")

while True:
    print("Please select the number of the following: ")
    print("1. Addition | 2. Subtraction | 3. Multiplication | 4. Division | 5. Exit")

    try:
        option = int(input("Input Option: "))
        match option:
            case 1:
                num1 = int(input("Enter First #: "))
                num2 = int(input("Enter Second #: "))
                ans = num1 + num2
                print(f"Result: {ans}")
            case 2:
                num1 = int(input("Enter First #: "))
                num2 = int(input("Enter Second #: "))
                ans = num1 - num2
                print(f"Result: {ans}")
            case 3:
                num1 = int(input("Enter First #: "))
                num2 = int(input("Enter Second #: "))
                ans = num1 * num2
                print(f"Result: {ans}")
            case 4:
                num1 = int(input("Enter First #: "))
                num2 = int(input("Enter Second #: "))
                if num2 == 0:
                    print("Can't divide by ZERO!")
                    break
                else:
                    ans = num1 / num2
                    print(f"Result: {ans}")
            case 5:
                print("Program Exiting......")
                break
            case _:
                print("Invalid choice! Please select a number from 1 to 4")
                continue

        choice = input("Do you want to continue? Yes or No: ")
        if choice.lower() not in ["yes", "y"]:
            break

    except ValueError:
        print("Invalid input. Please enter a valid number.")
