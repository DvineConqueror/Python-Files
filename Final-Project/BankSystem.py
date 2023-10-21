import os #Imported for the terminal screen clearing
import time #To add delay and effect
import pwinput #For secure password
import sys #For exiting
import re #For Password Checking Pattern

#Function to handle integer inputs to check if they are valid 
def number_inputs(prompt):
    while True:
        try:
            user_input = int(input(prompt))
            return user_input
        except ValueError:
            print("Invalid input!")
            time.sleep(1.0)
            clear_screen()
            bank_header()

#Function to clear screen/terminal
def clear_screen():
    os.system("cls")
    
#Function to display the header text    
def bank_header():
    print("********** Doynamic Finance **********")
   
#Function to display the main menu of the program   
def main_menu():
    print(f" ---------- Welcome! {accountName} ----------")
    print(f"   =========== Balance: {account_balance} ==========")
    print("    |[1]Deposit [2]Withdraw [3]Exit|    ")

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
                        print("Exiting the program...")
                        bank_header()
                        time.sleep(1.5)
                        return #to exit the function instead of going back to the while statement
                    elif choice_check == 2:
                        print("Going back to main page...")
                        bank_header()
                        time.sleep(1.5)
                        break
                    else:
                        print("Invalid")
                        bank_header()
                        time.sleep(1)
            case _:
                print("Invalid Choice")
                bank_header()
                time.sleep(1)

#Function to handle the creation of account process
def create_account():
    while True:
        clear_screen()
        bank_header()
        print("-------- Creating an account --------")
        print("Note: \n Password should be within 8 characters. \n It should contain ")
        
        #Collecting account information
        global userName
        global password
        global accountName
        accountFName = input("Enter your First Name: ")
        accountLName = input("Enter your Last Name: ")
        accountName = accountFName, accountLName
        personAge = number_inputs("Enter your Age: ")
        
        #Checking age eligibility
        if personAge < 18:
            print("Minimum Age of Account Holder is 18.")
            exit_system()
        elif personAge >= 18 and personAge < 122:
            userName = input("\nEnter your Username: ")
            while True:
                print("Note: \n Password should be within 8 characters. \n It should contain ")
                password = pwinput.pwinput(prompt='Enter your Password: ', mask='*')#to mask password
                if validate_password(password):
                    time.sleep(1.5)
                    print(f"Account: {accountName} has been created!")
                    print("proceeding to your account")
                    bank_header()
                    time.sleep(2)
                    login_account()
                else:
                    print("Invalid Password. \nPassword should contain at least one letter and one digit,\nand be at least 8 characters long.")
                    time.sleep(1)
        else:
            print("Invalid Age.")
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
    
#Function to handle the login authentication of account
def login_account():
    logged_in = False
    while not logged_in:
        clear_screen()
        bank_header()
        print("----------- Login Account ----------")
        userName_true = input("Enter your Username: ")
        password_true = pwinput.pwinput(prompt='Enter your Password: ', mask='*')#to mask password
        if userName != userName_true or password != password_true:
            print("Invalid username. Try again!")
            time.sleep(1.5)
        else:
            logged_in = True
            time.sleep(1.5)
            print("Account logged in, proceeding to your account")
            bank_header()
            time.sleep(1.2)
            clear_screen()
            bank_system()
            
#Defined Account Balance outside for balance checking
account_balance = 0 

#Function to handle the deposit process
def deposit():
    global account_balance
    password_attempt = pwinput.pwinput(prompt='Enter your password to continue: ', mask='*')
    
    if password_attempt == password:
        deposit_amount = number_inputs("Enter how much you want to deposit: ")

        if deposit_amount > 0:
            account_balance += deposit_amount
            print("You have successfully deposited:", deposit_amount)
            print("Going back to Menu...")
            time.sleep(1.5)
            clear_screen()
        else:
            print("Invalid amount to deposit!")
            time.sleep(1.2)
            clear_screen()
    else:
        print("Entered password is wrong.")
        exit_system()

#Function to handle the withdrawal process        
def withdraw():
    global account_balance
    password_attempt = pwinput.pwinput(prompt='Enter your password to continue: ', mask='*')
    
    if password_attempt == password:
        withdraw_amount = number_inputs("Enter how much you want to withdraw: ")

        if withdraw_amount > 0:
            if withdraw_amount <= account_balance:
                account_balance -= withdraw_amount
                print("Withdrawn amount is:", withdraw_amount)
                print("Going back to Menu...")
                time.sleep(1.5)
                clear_screen()
            else:
                print("Insufficient Funds!")
                retry = input("Would you like to continue? Yes|No: ").lower()
                if retry != 'yes':
                    exit_system()
                else:
                    print("Going back to menu...")
                    time.sleep(0.9)
                    clear_screen()
        else:
            print("Invalid amount to withdraw. Please enter a positive amount.")
            time.sleep(1.5)
            clear_screen()
    else:
        print("Entered password is wrong.")
        exit_system()
        
def exit_system():
    print("System Exiting...")
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
                password_attempt = pwinput.pwinput(prompt='Enter your password to continue: ', mask='*')
                if password_attempt == password:
                    print("System Exiting...")
                    time.sleep(1)
                    return False
                else:
                    print("Entered password is wrong.")
                    time.sleep(0.5)
                    print("System Exiting...")
                    time.sleep(1)
                    return False
            case _:
                print("Invalid Choice")
                bank_header()
                time.sleep(1)
                clear_screen()
                
#Initiating login process        
login()
        
    