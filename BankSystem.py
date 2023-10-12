import os #imported for the terminal screen clearing
import time #to add delay and effect
import pwinput #for secure password

def create_account():
    os.system("cls")
    print("DOMINIC BANKING SYSTEM")
    print("Creating Account")
    global userName
    global password
    userName = input("Enter your username: ")
    password = pwinput.pwinput(prompt='Enter your password: ', mask='*')#to mask password
    print(f"Account: {userName} has been created!")
    time.sleep(2) #2 seconds of delay
    login_account()
    
def login_account():
    logged_in = False
    while not logged_in:
        os.system("cls")
        print("DOMINIC BANKING SYSTEM")
        print("Login Account")
        userName_true = input("Enter your username: ")
        password_true = pwinput.pwinput(prompt='Enter your password: ', mask='*')#to mask password
        if userName != userName_true or password != password_true:
            print("Invalid username. Try again!")
            time.sleep(1.5)
        else:
            logged_in = True
            bank_system()
            
account_balance = 0 #Defined Account Balance outside
  
def bank_system():
    
    global account_balance #declare account balance to global to continuously update when the program checks balance
    
    while True:
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
                else:
                    print("Invalid amount to deposit")
                    os.system("cls")
            case 2:
                withdraw = int(input("Enter how much you want to withdraw: "))
                if withdraw <= account_balance:
                    account_balance -= withdraw
                    print("Withdrawn amount is: ", withdraw)
                    time.sleep(2)
                    os.system("cls")
                else:
                    print("Insufficient Funds!")
                    retry = input("Would you like to continue? yes/no: ")
                    if retry.lower() != 'yes':
                        print("Have a nice day!")
                        time.sleep(1.5)
                        print("Bank System exiting...")
                        break
                    else:
                        os.system("cls")
                        continue
            case 3:
                print("Bank System exiting...")
                return True   
    
def login():
    while True:
        os.system("cls")
        print("DOMINIC BANKING SYSTEM")
        print("Would you like create an account?")
        choice = input("Enter your choice: ")
        match choice.lower():
            case 'yes':
                print("Creating account in a few seconds...")
                time.sleep(1.5)
                create_account()
                break
            case 'no':
                print("You can't proceed without an account.")
                while True:
                    choice_check = input("Would you like to exit the application: ").lower()
                    if choice_check == 'yes':
                        print("Exiting the program...")
                        time.sleep(1.5)
                        return #to exit the function instead of going back to the while statement
                    elif choice_check == 'no':
                        print("Going back to main page...")
                        time.sleep(1.5)
                        break
            case _:
                print("Invalid Choice")
    
        
login()
        
    