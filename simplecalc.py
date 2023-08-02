print ("Dominic's Simple Calculator!")
print ("Please select the number of the following: ")
print ("1. Addition | 2. Subtraction | 3. Multiplication | 4. Division")

option = int(input("Input Option: "))
match option:
    case 1:
        num1 = int(input("Enter First #: "))
        num2 = int(input("Enter Second #: "))
        ans = num1 + num2
        print (ans)
    case 2:
        num1 = int(input("Enter First #: "))
        num2 = int(input("Enter Second #: "))
        ans = num1 - num2
        print (ans)
    case 3:
        num1 = int(input("Enter First #: "))
        num2 = int(input("Enter Second #: "))
        ans = num1 * num2
        print (ans)
    case 4:
        num1 = int(input("Enter First #: "))
        num2 = int(input("Enter Second #: "))
        ans = num1 / num2
        print (ans)