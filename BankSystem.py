import os #imported for the terminal screen clearing
import time #to add delay and effect

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
    time.sleep(2) #2 seconds of delay
    login_account()
    
def login_account():
    while login_account != False:
        os.system("cls")
        print("DOMINIC BANKING SYSTEM")
        print("Login Account")
        userName_true = input("Enter your username: ")
        password_true = input("Enter your password: ")
        print("======================")
        
        if userName != userName_true or password != password_true:
            print("Invalid username. Try again!")
            time.sleep(2)
        else:
            bank_system()
      
account_balance = 0 #Defined Account Balance outside
  
def bank_system():
    
    global account_balance #declare account balance to global to continuously update when the program checks balance
    
    print("DOMINIC BANKING SYSTEM")
    print("Welcome!", userName)
    print("Menu")
    print("Balance:", account_balance)
    print("[1]Deposit [2]Withdraw [3]Exit")
    choice = int(input("Enter your choice: "))
    
    match choice:
        case 1:
            deposit = int(input("Enter how much you want to deposit: "))
            if deposit > 0:
                account_balance += deposit
                print("You have successfully deposited:", deposit)
                time.sleep(2)
                os.system("cls")
                bank_system()
            else:
                print("Invalid amount to deposit")
        case 2:
            withdraw = int(input("Enter how much you want to withdraw: "))
            if withdraw <= account_balance:
                account_balance -= withdraw
                print("Withdrawn amount is: ", withdraw)
                time.sleep(2)
                os.system("cls")
                bank_system()
            else:
                print("Invalid amount to withdraw")
                retry = input("Would you like to continue? yes/no: ")
                if retry.lower() != 'yes':
                    print("Have a nice day!")
                else:
                    os.system("cls")
                    bank_system()
        case 3:
            print("Bank System exiting...")
            time.sleep(2)
            os.system("cls")         
    
def login():
    print("DOMINIC BANKING SYSTEM")
    print("1) Create Account")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        create_account()
    else:
        print("Invalid")
    print("======================")
        
login()
        
    