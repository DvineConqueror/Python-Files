import customtkinter
import sys
from tkinter import messagebox
from tkinter import Toplevel

customtkinter.set_appearance_mode("black")
customtkinter.set_default_color_theme("green")

#Global Variables
attempts = 0  # Move the attempts variable outside the function
balance = 0
transaction_choice = None

def main_menu():
    global balance
    main_menu_window = customtkinter.CTk()
    main_menu_window.geometry("400x350")
    
    frame_create = customtkinter.CTkFrame(master=main_menu_window)
    frame_create.pack_propagate(False)
    frame_create.pack(pady=0, padx=0, fill="both", expand=True)

    header_label = customtkinter.CTkLabel(master=frame_create, text="Doynamic Bank", font=("Constantia", 52), text_color="#1DDEA8")
    header_label.pack(pady=(15, 0), padx=10)
    
    balance_label = customtkinter.CTkLabel(master=frame_create, text=f"Balance: ₱ {balance}", font=("Arial", 24))
    balance_label.pack(pady=(15, 0), padx=10)
    
    def set_transaction_choice(choice):
        global transaction_choice
        transaction_choice = choice
        verify()
    
    def verify():
        create_window = Toplevel(main_menu_window)
        create_window.geometry("400x300")
        create_window.resizable(0,0)
        create_window.title("Doynamic Banking")
        
        frame_login = customtkinter.CTkFrame(master=create_window)
        frame_login.pack(pady=0, padx=0, fill="both", expand=True)

        verify_label = customtkinter.CTkLabel(master=frame_login, text="Verification", font=("Constantia", 52), text_color="#DA5D74")
        verify_label.pack(pady=12, padx=10)

        text_label = customtkinter.CTkLabel(master=frame_login, text="Enter your password for verification", font=("Constantia", 20))
        text_label.pack(pady=12, padx=10)

        password_login = customtkinter.CTkEntry(master=frame_login, placeholder_text="Password", show="*", font=("Arial", 18), width=205)
        password_login.pack(pady=12, padx=10)
        
        def toggle_password():
            current_value = password_login.cget('show')
            if current_value == '':
                password_login.configure(show='*')
            else:
                password_login.configure(show='')

        def login_attempt():
            global attempts
            global exit_system
            entered_password = password_login.get()

            if created_password == entered_password:
                messagebox.showinfo("Login Successful", "Welcome to the Doynamic Bank!")
                create_window.destroy()  # Close the login window
                
                if transaction_choice == "deposit":
                    deposit()
                elif transaction_choice == "withdraw":
                    withdraw_money()
            else:
                attempts += 1
                if attempts > 3:
                    messagebox.showerror("Login failed", "Too many failed attempts!")
                    exit_system()
                messagebox.showerror("Login Failed", "Please check your credentials.")

        checkbox = customtkinter.CTkCheckBox(master=frame_login, text="Show password", command=toggle_password, onvalue="on", offvalue="off")
        checkbox.pack(padx=0, pady=10)

        login_button = customtkinter.CTkButton(master=frame_login, border_color="#000000", text="Login", command=login_attempt, font=("Constantia", 14), width=200)
        login_button.pack(pady=12, padx=10)
        create_window.bind("<Return>", lambda event=None: login_attempt())
        main_menu_window.withdraw()
    
    def deposit():
        create_window_deposit = Toplevel(main_menu_window)
        create_window_deposit.geometry("400x300")
        create_window_deposit.resizable(0,0)
        create_window_deposit.title("Doynamic Banking")
        
        frame_login = customtkinter.CTkFrame(master=create_window_deposit)
        frame_login.pack(pady=0, padx=0, fill="both", expand=True)

        label_login = customtkinter.CTkLabel(master=frame_login, text="Deposit Money", font=("Constantia", 52), text_color="#1DDEA8")
        label_login.pack(pady=12, padx=10)
        
        label_login = customtkinter.CTkLabel(master=frame_login, text="Enter the amount you want to deposit:", font=("Constantia", 20))
        label_login.pack(pady=12, padx=10)

        deposit_amount = customtkinter.CTkEntry(master=frame_login, placeholder_text="Amount", font=("Arial", 18), width=205)
        deposit_amount.pack(pady=12, padx=10)
        
        def update_balance():
            global balance
            check_deposit = deposit_amount.get()
            try:
                check_deposit = float(check_deposit)
                if check_deposit > 0:
                    balance += check_deposit
                    messagebox.showinfo("Doynamic Banking", f"You have successfully deposited: ₱{check_deposit}")
                    create_window_deposit.destroy()  # Close the deposit window
                    main_menu()
                else:
                    messagebox.showerror("Doynamic Banking", "Invalid amount to deposit!")
            except ValueError:
                messagebox.showerror("Doynamic Banking", "Please enter a valid numeric amount.")

        deposit_button = customtkinter.CTkButton(master=frame_login, border_color="#000000", text="Ok", command=update_balance, font=("Constantia", 14), width=20)
        deposit_button.pack(pady=12, padx=10)
        deposit_button.bind("<Return>", lambda event=None: update_balance())
        main_menu_window.withdraw()
    
    def withdraw_money():
        root.withdraw()
        create_window_withdraw = Toplevel(main_menu_window)
        create_window_withdraw.geometry("400x300")
        create_window_withdraw.resizable(0,0)
        create_window_withdraw.title("Doynamic Banking")
        
        frame_login = customtkinter.CTkFrame(master=create_window_withdraw)
        frame_login.pack(pady=0, padx=0, fill="both", expand=True)

        label_login = customtkinter.CTkLabel(master=frame_login, text="Withdraw Money", font=("Constantia", 48), text_color="#1DDEA8")
        label_login.pack(pady=12, padx=10)
        
        label_login = customtkinter.CTkLabel(master=frame_login, text="Enter the amount you want to withdraw:", font=("Constantia", 20))
        label_login.pack(pady=12, padx=10)

        withdraw_amount = customtkinter.CTkEntry(master=frame_login, placeholder_text="Amount", font=("Arial", 18))
        withdraw_amount.pack(pady=12, padx=10)
        
        def update_balance():
            global balance
            check_withdraw = withdraw_amount.get()
            try:
                check_withdraw = float(check_withdraw)
                if check_withdraw > 0:
                    if check_withdraw <= balance:
                        balance -= check_withdraw
                        messagebox.showinfo("Doynamic Banking", f"You have successfully withdrawn: ₱{check_withdraw}")
                        create_window_withdraw.destroy()
                        main_menu()
                    else:
                        messagebox.showerror("Doynamic Banking", "Insufficient amount to deposit!")
                        create_window_withdraw.destroy()
                        main_menu()
                else:
                    messagebox.showerror("Doynamic Banking", "Insufficient amount to deposit!")
                    create_window_withdraw.destroy()
                    main_menu()
            except ValueError:
                messagebox.showerror("Doynamic Banking", "Please enter a valid numeric amount.")
                
        withdraw_button = customtkinter.CTkButton(master=frame_login, border_color="#000000", text="Ok", command=update_balance, font=("Constantia", 14), width=50)
        withdraw_button.pack(pady=12, padx=10)
        withdraw_button.bind("<Return>", lambda event=None: update_balance())
        main_menu_window.withdraw()
    
    select_deposit_button = customtkinter.CTkButton(master=frame_create, border_color="red", text="Deposit Money", command=lambda: set_transaction_choice("deposit"), font=("Constantia", 20), width=180, height=35)
    select_deposit_button.pack(pady=(16, 14), padx=10)
    
    select_withdraw_button = customtkinter.CTkButton(master=frame_create, border_color="red", text="Withdraw Money", command=lambda: set_transaction_choice("withdraw"), font=("Constantia", 20), width=180, height=35)
    select_withdraw_button.pack(pady=(12, 14), padx=10)
    
    exit_button = customtkinter.CTkButton(master=frame_create, border_color="red", text="Exit", command=lambda:exit_system(), font=("Constantia", 20), width=180, height=35)
    exit_button.pack(pady=12, padx=10)
    
    main_menu_window.mainloop()
    
def exit_system():
    messagebox.showinfo("Doynamic Banking", "Thank you for using Doynamic Bank!")
    sys.exit(0)

def validate_password(password):
    if len(password) < 8:
        return False
    if not any(c.islower() for c in password):
        return False
    if not any(c.isupper() for c in password):
        return False
    if not any(c.isdigit() for c in password):
        return False
    return True

def create_account_section():
    create_window = Toplevel(root)
    create_window.geometry("400x350")
    create_window.resizable(0,0)
    create_window.title("Doynamic Banking")
    root.withdraw()

    frame_create = customtkinter.CTkFrame(master=create_window)
    frame_create.pack_propagate(False)
    frame_create.pack(pady=0, padx=0, fill="both", expand=True)

    label_create = customtkinter.CTkLabel(master=frame_create, text="Create an account", font=("Constantia", 42), text_color="#1DDEA8")
    label_create.pack(pady=(5, 0), padx=10)
    
    note = customtkinter.CTkLabel(master=frame_create, text="Password should contain:", text_color="#DA5D74",font=("Constantia", 20))
    note.pack(pady=(0, 0))
    
    label_remind = customtkinter.CTkLabel(master=frame_create, text="\nMinimum of 8 Characters\nOne Uppercase Letter\nOne Numeric Value",font=("Constantia", 16))
    label_remind.pack(pady=(0, 0))

    username_create = customtkinter.CTkEntry(master=frame_create, placeholder_text="Username", font=("Arial", 18), width=200)
    username_create.pack(pady=(12, 0), padx=10)

    password_create = customtkinter.CTkEntry(master=frame_create, placeholder_text="Password", show="*", font=("Arial", 18), width=200)
    password_create.pack(pady=(22, 0), padx=10)

    def toggle_password():
        current_value = password_create.cget('show')
        if current_value == '':
            password_create.configure(show='*')
        else:
            password_create.configure(show='')

    def create_account():
        global created_username
        global created_password
        created_username = username_create.get()
        created_password = password_create.get()

        if validate_password(created_password):
            messagebox.showinfo("Account Created", "Account created successfully!")
            login_account_section()
            create_window.destroy()  # Close the create window
        else:
            messagebox.showerror("Invalid Password", "Password does not meet the criteria.")

    checkbox = customtkinter.CTkCheckBox(master=frame_create, text="Show password", command=toggle_password, onvalue="on", offvalue="off")
    checkbox.pack(padx=0, pady=10)

    create_account_button = customtkinter.CTkButton(master=frame_create, border_color="red", text="Create Account", command=create_account, font=("Constantia", 20))
    create_account_button.pack(pady=(12, 0), padx=10)
    create_window.bind("<Return>", lambda event=None: create_account())

def login_account_section():
    login_window = Toplevel(root)
    login_window.geometry("400x350")
    login_window.resizable(0, 0)
    login_window.title("Doynamic Banking")

    frame_login = customtkinter.CTkFrame(master=login_window)
    frame_login.pack(pady=0, padx=0, fill="both", expand=True)

    label_login = customtkinter.CTkLabel(master=frame_login, text="Login", font=("Constantia", 42), text_color="#1DDEA8")
    label_login.pack(pady=12, padx=10)
    
    label_login1 = customtkinter.CTkLabel(master=frame_login, text="Enter your login credentials: ", font=("Constantia", 20))
    label_login1.pack(pady=12, padx=10)

    username_login = customtkinter.CTkEntry(master=frame_login, placeholder_text="Username", font=("Arial", 18), width=200)
    username_login.pack(pady=12, padx=10)

    password_login = customtkinter.CTkEntry(master=frame_login, placeholder_text="Password", show="*", font=("Arial", 18), width=205)
    password_login.pack(pady=12, padx=10)
    
    def toggle_password():
        current_value = password_login.cget('show')
        if current_value == '':
            password_login.configure(show='*')
        else:
            password_login.configure(show='')

    def login_attempt():
        global exit_system
        global attempts
        entered_username = username_login.get()
        entered_password = password_login.get()

        if created_username == entered_username and created_password == entered_password:
            messagebox.showinfo("Login Successful", "Welcome to the Doynamic Bank!")
            login_window.destroy()  # Close the login window
            main_menu()
        elif created_username == entered_username and created_password != entered_password:
            attempts += 1
            if attempts > 3:
                messagebox.showerror("Login failed", "Too many failed attempts!")
                exit_system()
            messagebox.showerror("Login Failed", "Please check your password!")
        elif created_username != entered_username and created_password == entered_password:
            attempts += 1
            if attempts > 3:
                messagebox.showerror("Login failed", "Too many failed attempts!")
                exit_system()
            messagebox.showerror("Login Failed", "Please check your username!")
        else:
            attempts += 1
            if attempts > 3:
                messagebox.showerror("Login failed", "Too many failed attempts!")
                exit_system()
            messagebox.showerror("Login Failed", "Please check your credentials.")

    checkbox = customtkinter.CTkCheckBox(master=frame_login, text="Show password", command=toggle_password, onvalue="on", offvalue="off")
    checkbox.pack(padx=0, pady=10)

    login_button = customtkinter.CTkButton(master=frame_login, border_color="#000000", text="Login", command=login_attempt, font=("Constantia", 14), width=200)
    login_button.pack(pady=12, padx=10)
    login_window.bind("<Return>", lambda event=None: login_attempt())

root = customtkinter.CTk()
root.geometry("400x350")
root.resizable(0,0)
root.title("Welcome to Doynamic Bank!")

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=0, padx=0,side="left", fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text="Doynamic \nBank", font=("Constantia", 50))
label.pack(pady=10, padx=25)

label = customtkinter.CTkLabel(master=frame, text="Would you like to", font=("Constantia", 20))
label.pack(pady=(15,0), padx=30)

create_button = customtkinter.CTkButton(master=frame, fg_color="#21866A", text="Create Account", command=lambda:create_account_section(), font=("Constantia", 20), width=180, height=40)
create_button.pack(pady=(19,6), padx=10)

exit_button = customtkinter.CTkButton(master=frame, border_color="red", text="Exit", command=lambda:exit_system(), font=("Constantia", 20), width=180, height=35)
exit_button.pack(pady=(14,3), padx=10)

root.mainloop()
