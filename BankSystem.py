import os
def create_account():
    os.system("cls")
    print("DOMINIC BANKING SYSTEM")
    print("Creating Account")
    global userName
    global password
    userName = input("Enter your username: ")
    password = input("Enter your password: ")
    print("Account: ", userName, "has been created!")
    print("======================")
    
def login_account():
    os.system("cls")
    print("DOMINIC BANKING SYSTEM")
    print("Login Account")
    userName_true = input("Enter your username: ")
    password_true = input("Enter your password: ")
    print("======================")
    
    if userName != userName_true or password != password_true:
        print("Invalid username. Try again!")
        return
    else:
        bank_system()
        
def bank_system():
    money = 0
    os.system("cls")
    print("DOMINIC BANKING SYSTEM")
    print("Welcome!", userName)
    print("Menu")
    print("[1]Deposit [2]Withdraw [3] Show Balance [4] Exit")
    choice = int(input("Enter your choice: "))
    
    match choice:
        case 1:
            deposit = int(input("Enter how much you want to deposit: "))
            if deposit > 0:
                money += deposit
                print("Balance is: ", money)
                bank_system()
            else:
                print("Invalid amount to deposit")
        case 2:
            print("Current Balance is:", money)
            withdraw = int(input("Enter how much you want to withdraw: "))
            if withdraw < money:
                withdraw -= money
                print("Withdrawn amount is: ", withdraw)
                print("Current balance is: ", money)
                bank_system()
            else:
                print("Invalid amount to withdraw")
                retry = input("Would you like to continue? yes/no: ")
                if retry.lower() != 'yes':
                    print("Have a nice day!")
                else:
                    bank_system()
        case 3:
            print("Your current balance is: ", money)
            retry = input("Would you like to continue? yes/no: ")
            if retry.lower() != 'yes':
                print("Have a nice day!")
            else:
                bank_system()
        case 4:
            print("Bank System exiting...")
    
def login():
    print("DOMINIC BANKING SYSTEM")
    print("1) Create Account")
    print("2) Login Account")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        create_account()
    elif choice == 2:
        login_account()
    print("======================")
        
login()
        
    