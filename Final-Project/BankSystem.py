import os #imported for the terminal screen clearing
import time #to add delay and effect
import pwinput #for secure password

def login():
    while True:
        os.system("cls")
        print("********** Doynamic Finance **********")
        print("Would you like to create an account?")
        print("1. Yes")
        print("2. No")
        choice = input("Enter your choice: ")#these are in string, they should accept a string instead of int
        match choice:
            case "1":
                print("Creating account in a few seconds...")
                print("********** Doynamic Finance **********")
                time.sleep(1.5)
                create_account()
                break
            case "2":
                print("You can't proceed without an account.")
                print("Would you like to exit the program?")
                print("1. Yes")
                print("2. No")
                while True:
                    choice_check = input("Input your choice: ")
                    if choice_check == "1":
                        print("Exiting the program...")
                        print("********** Doynamic Finance **********")
                        time.sleep(1.5)
                        return #to exit the function instead of going back to the while statement
                    elif choice_check == "2":
                        print("Going back to main page...")
                        print("********** Doynamic Finance **********")
                        time.sleep(1.5)
                        break
                    else:
                        print("Invalid")
                        print("********** Doynamic Finance **********")
                        time.sleep(1)
            case _:
                print("Invalid Choice")
                print("********** Doynamic Finance **********")
                time.sleep(1)

def create_account():
    os.system("cls")
    print("********** Doynamic Finance **********")
    print("-------- Creating an account --------")
    global userName
    global password
    userName = input("Enter your username: ")
    password = pwinput.pwinput(prompt='Enter your password: ', mask='*')#to mask password
    time.sleep(1.5)
    print(f"Account: {userName} has been created!")
    print("********** Doynamic Finance **********")
    time.sleep(2) #2 seconds of delay
    login_account()
    
def login_account():
    logged_in = False
    while not logged_in:
        os.system("cls")
        print("********** Doynamic Finance **********")
        print("----------- Login Account ----------")
        userName_true = input("Enter your username: ")
        password_true = pwinput.pwinput(prompt='Enter your password: ', mask='*')#to mask password
        if userName != userName_true or password != password_true:
            print("Invalid username. Try again!")
            time.sleep(1.5)
        else:
            logged_in = True
            time.sleep(1.5)
            print("Account logged in, proceeding to your account")
            print("********** Doynamic Finance **********")
            time.sleep(1.2)
            os.system("cls")
            bank_system()
            
account_balance = 0 #Defined Account Balance outside

def bank_system():
    
    global account_balance #declare account balance to global to continuously update when the program checks balance
    
    while True:
        print("********** Doynamic Finance **********")
        print(f"---------- Welcome! {userName} ----------")
        print(f"=========== Balance: {account_balance} ==========")
        print("+++|[1]Deposit [2]Withdraw [3]Exit|+++")
        choice = input("Enter your choice: ")
        
        password_attempt = pwinput.pwinput(prompt='Enter your password to continue: ', mask='*')
    
        match choice:
            case "1":
                deposit = int(input("Enter how much you want to deposit: "))
                if deposit > 0:
                    if password_attempt == password:
                        account_balance += deposit
                        time.sleep(1.5)
                        print("You have successfully deposited:", deposit)
                        print("Going back to Menu...")
                        time.sleep(1.5)
                        os.system("cls")
                    else:
                        print("Entered password is wrong.")
                        print("Terminating Operation")
                        print("Have a nice day!")
                        print("********** Doynamic Finance **********")
                        time.sleep(1.2)
                        break
                else:
                    print("Invalid amount to deposit")
                    time.sleep(1.2)
                    os.system("cls")
            case "2":
                withdraw = int(input("Enter how much you want to withdraw: "))
                if withdraw <= account_balance:
                    if password_attempt == password:
                        account_balance -= withdraw
                        time.sleep(1.5)
                        print("Withdrawn amount is: ", withdraw)
                        print("Going back to Menu...")
                        time.sleep(1.5)
                        os.system("cls")
                    else:
                        print("Entered password is wrong.")
                        print("Terminating Operation")
                        print("Have a nice day!")
                        print("********** Doynamic Finance **********")
                        time.sleep(1.2)
                        break
                else:
                    print("Insufficient Funds!")
                    retry = input("Would you like to continue? yes/no: ")
                    if retry.lower() != 'yes':
                        print("Program exiting...")
                        time.sleep(1.5)
                        print("Have a nice day!")
                        print("********** Doynamic Finance **********")
                        break
                    else:
                        os.system("cls")
                        continue
            case "3":
                if password_attempt == password:
                    print("Bank System exiting...")
                    print("********** Doynamic Finance **********")
                    time.sleep(0.9)
                    return True
                else:
                        print("Entered password is wrong.")
                        time.sleep(1.5)
                        os.system("cls")
        
login()
        
    