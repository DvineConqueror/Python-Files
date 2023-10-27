import os #Imported for the terminal screen clearing
import time #To add delay and effect
import pwinput #For secure password
import sys #For exiting
import re #For Password Checking Pattern
from colorama import Fore, Back, Style, init

init(autoreset=True)

#Function to handle integer inputs to check if they are valid 
def number_inputs(prompt):
    while True:
        try:
            user_input = int(input(prompt))
            return user_input
        except ValueError:
            print(Fore.RED + "Invalid input!")
            time.sleep(1.0)
            clear_screen()
            bank_header()

#Function to clear screen/terminal
def clear_screen():
    os.system("cls")
    
#Function to display the header text    
def bank_header():
    print(Fore.GREEN +"********** Doynamic Finance **********")
   
#Function to display the main menu of the program   
def main_menu():
    print(Fore.LIGHTCYAN_EX + f"   ----- Welcome! {accountName} -----")
    print(Fore.LIGHTBLUE_EX + f"   =========== Balance: {account_balance} ==========")
    print(Fore.LIGHTYELLOW_EX + "    |[1]Deposit [2]Withdraw [3]Exit|    ")

#Function to handle the login process
def login():
    while True:
        clear_screen()
        bank_header()
        print("Would you like to proceed?")
        print("1. Create an account")
        print("2. Not create an account")
        choice = number_inputs("Enter your choice: ")#calling num inputs to better the error handling when string is inputted
        match choice:
            case 1:
                print("Creating account in a few seconds...")
                bank_header()
                time.sleep(1.5)
                create_account()
                break
            case 2:
                print("You can't proceed without an account.")
                print("Would you like to exit the program?")
                print("1. Yes")
                print("2. No")
                while True:
                    choice_check = number_inputs("Input your choice: ")
                    if choice_check == 1:
                        print(Fore.RED + "Exiting the program...")
                        bank_header()
                        time.sleep(1.5)
                        return #to exit the function instead of going back to the while statement
                    elif choice_check == 2:
                        print("Going back to main page...")
                        bank_header()
                        time.sleep(1.5)
                        break
                    else:
                        print(Fore.RED + "Invalid Input")
                        bank_header()
                        time.sleep(1)
            case _:
                print(Fore.RED + "Invalid Choice")
                bank_header()
                time.sleep(1)

#Function to handle the creation of account process
def create_account():
    while True:
        clear_screen()
        bank_header()
        print("-------- Creating an account --------")
        
        #Collecting account information
        global userName
        global password
        global accountName
        accountFName = input("Enter your First Name: ")
        accountLName = input("Enter your Last Name: ")
        accountName = f"{accountFName} {accountLName}"
        personAge = number_inputs("Enter your Age: ")
        
        #Checking age eligibility
        if personAge < 18:
            print(Fore.RED + "Minimum Age of Account Holder is 18.")
            exit_system()
        elif personAge >= 18 and personAge < 122:
            userName = input("\nEnter your Username: ")
            while True:
                print("Note: \n Password should be within 8 characters. \n It should contain ")
                password = pwinput.pwinput(prompt='Enter your Password: ', mask='*')#to mask password
                if validate_password(password):
                    time.sleep(1.5)
                    print(Fore.LIGHTCYAN_EX + f"Account: {accountName} has been created!")
                    print(Fore.LIGHTGREEN_EX + "proceeding to your account")
                    bank_header()
                    time.sleep(2)
                    login_account()
                    return False
                else:
                    clear_screen()
                    print(Fore.RED + "Invalid Password. \nPassword should contain at least one letter and one digit,\nand be at least 8 characters long.")
                    time.sleep(1)
    
#For password validation    
def validate_password(password):  
    if len(password) < 8:  
        return False  
    if not re.search("[a-z]", password):  
        return False  
    if not re.search("[A-Z]", password):  
        return False  
    if not re.search("[0-9]", password):  
        return False  
    return True    

def password_attempt():
    attempts = 0
    global max_attempts
    password_input = pwinput.pwinput(prompt='Enter your password to continue: ', mask='*')

    while attempts <= max_attempts:
        if password_input == password:
            return True
        else:
            print(Fore.RED + "Entered password is wrong. Try again!")
            attempts += 1
            time.sleep(1.5)
            password_input = pwinput.pwinput(prompt='Enter your password to continue: ', mask='*')

    print(Fore.RED + f"Too many attempts. Exiting the system.")
    time.sleep(1.5)
    exit_system()  
    
#Function to handle the login authentication of account
def login_account():
    attempts = 0
    max_attempts = 3
    logged_in = False   
    while not logged_in and attempts <= max_attempts:
        clear_screen()
        bank_header()
        print("----------- Login Account ----------")
        userName_true = input("Enter your Username: ")
        password_true = pwinput.pwinput(prompt='Enter your Password: ', mask='*')#to mask password
        if userName != userName_true or password != password_true:
            print(Fore.RED + "Invalid user credentials. Try again!")
            attempts += 1
            time.sleep(1.5)
        else:
            logged_in = True
            time.sleep(1.5)
            print(Fore.LIGHTGREEN_EX + "Account logged in, proceeding to your account")
            bank_header()
            time.sleep(1.2)
            clear_screen()
            bank_system()
    if attempts > max_attempts:
        print(Fore.RED + f"Too many attempts. Exiting the system.")
        time.sleep(1.5)
        exit_system
            
#Defined Account Balance outside for balance checking
account_balance = 0
max_attempts = 3

#Function to handle the deposit process
def deposit():
    global account_balance

    if password_attempt():
        deposit_amount = number_inputs("Enter how much you want to deposit: ")

        if deposit_amount > 0:
            account_balance += deposit_amount
            print(Fore.CYAN +"You have successfully deposited:", Fore.GREEN + deposit_amount)
            print(Fore.LIGHTGREEN_EX + "Going back to Menu...")
            time.sleep(1.5)
            clear_screen()
        else:
            print(Fore.RED + "Invalid amount to deposit!")
            time.sleep(1.2)
            clear_screen()
    else:
        print(Fore.RED + "Password attempts exceeded. Exiting the system...")
        exit_system()

#Function to handle the withdrawal process        
def withdraw():
    global account_balance
    if password_attempt():
        withdraw_amount = number_inputs("Enter how much you want to withdraw: ")

        if withdraw_amount > 0:
            if withdraw_amount <= account_balance:
                account_balance -= withdraw_amount
                print("Withdrawn amount is:", Fore.GREEN + withdraw_amount)
                print("Going back to Menu...")
                time.sleep(1.5)
                clear_screen()
            else:
                print(Fore.RED + "Insufficient Funds!")
                retry = input("Would you like to continue? Yes|No: ").lower()
                if retry != 'yes':
                    exit_system()
                else:
                    print("Going back to menu...")
                    time.sleep(0.9)
                    clear_screen()
        else:
            print(Fore.RED + "Invalid amount to withdraw. Please enter a positive amount.")
            time.sleep(1.5)
            clear_screen()
    else:
        print(Fore.RED + "Password attempts exceeded. Exiting the system...")
        exit_system()
        
def exit_system():
    print(Fore.RED + "System Exiting...")
    time.sleep(1.2)
    bank_header()
    time.sleep(0.5)
    sys.exit(0)

#Function to handle the main banking system        
def bank_system():
    while True:
        bank_header()
        main_menu()
        choice = number_inputs("Enter your choice: ")
        match choice:
            case 1:
                deposit()
            case 2:
                withdraw()
            case 3:
                time.sleep(1)
                exit_system()
            case _:
                print(Fore.RED + "Invalid Choice")
                bank_header()
                time.sleep(1)
                clear_screen()
                
#Initiating login process        
login()
        
    