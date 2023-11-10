import customtkinter
import os
from PIL import ImageTk
from tkinter import messagebox
from tkinter import Toplevel

customtkinter.set_appearance_mode("black")
customtkinter.set_default_color_theme("green")

def main_menu():
    main_menu_window = customtkinter.CTk()
    main_menu_window.geometry("600x400")
    main_menu_window.mainloop()
    
def exit_system():
    messagebox.showinfo("Doynamic Banking", "Thank you for using Doynamic Bank!")
    exit()

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
    create_window = Toplevel(root, background="black")
    create_window.geometry("400x300")
    create_window.resizable(0,0)
    create_window.title("Create Account")
    sv = customtkinter.StringVar()
    root.withdraw()

    frame_create = customtkinter.CTkFrame(master=create_window)
    frame_create.pack_propagate(False)
    frame_create.pack(pady=0, padx=0, fill="both", expand=True)

    label_create = customtkinter.CTkLabel(master=frame_create, text="Create an account", font=("Times", 32), text_color="#1DDEA8")
    label_create.pack(pady=(5, 0), padx=10)
    
    note = customtkinter.CTkLabel(master=frame_create, text="Password should contain:", text_color="#DA5D74",font=("Times", 20))
    note.pack(pady=(0, 0))
    
    label_remind = customtkinter.CTkLabel(master=frame_create, text="\nMinimum of 8 Characters, One Uppercase Letter\nOne Numeric Value",font=("Times", 14))
    label_remind.pack(pady=(0, 0))

    username_create = customtkinter.CTkEntry(master=frame_create, placeholder_text="Username", font=("Times", 18), width=200)
    username_create.pack(pady=(12, 0), padx=10)

    password_create = customtkinter.CTkEntry(master=frame_create, placeholder_text="Password", show="*", font=("Times", 18), width=200)
    password_create.pack(pady=(22, 0), padx=10)

    def toggle_password():
        current_value = password_create.cget('show')
        if current_value == '':
            password_create.configure(show='*')
        else:
            password_create.configure(show='')
    
    checkbox = customtkinter.CTkCheckBox(master=frame_create, text="Show password", command=toggle_password, onvalue="on", offvalue="off")
    checkbox.pack(padx=0, pady=10)

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

    create_button = customtkinter.CTkButton(master=frame_create, border_color="red", text="Create Account", command=create_account, font=("Times", 20))
    create_button.pack(pady=(2, 0), padx=10)
    create_window.bind("<Return>", lambda event=None: create_account())

attempts = 0  # Move the attempts variable outside the function

def login_account_section():
    login_window = Toplevel(root)
    login_window.geometry("400x300")
    login_window.resizable(0, 0)
    login_window.title("Login")

    frame_login = customtkinter.CTkFrame(master=login_window)
    frame_login.pack(pady=0, padx=0, fill="both", expand=True)

    label_login = customtkinter.CTkLabel(master=frame_login, text="Login", font=("Times", 32))
    label_login.pack(pady=12, padx=10)

    username_login = customtkinter.CTkEntry(master=frame_login, placeholder_text="Username", font=("Times", 18), width=200)
    username_login.pack(pady=12, padx=10)

    password_login = customtkinter.CTkEntry(master=frame_login, placeholder_text="Password", show="*", font=("Times", 18), width=205)
    password_login.pack(pady=12, padx=10)

    def login_attempt():
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

    login_button = customtkinter.CTkButton(master=frame_login, border_color="#000000", text="Login", command=login_attempt, font=("Times", 14), width=200)
    login_button.pack(pady=12, padx=10)
    login_window.bind("<Return>", lambda event=None: login_attempt())

root = customtkinter.CTk()
root.geometry("400x260")
root.resizable(0,0)
root.title("Welcome to Doynamic Bank!")
root.iconpath = ImageTk.PhotoImage(file=os.path.join("Final-Project","BankLogo.png"))
root.wm_iconbitmap()
root.iconphoto(False, root.iconpath)

left_frame = customtkinter.CTkFrame(master=root, width=100)
left_frame.pack(padx=0, pady=0, side="left", fill="y", expand=True)

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=0, padx=0,side="left", fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text="Doynamic Bank", font=("Times", 38))
label.pack(pady=12, padx=30)


label = customtkinter.CTkLabel(master=frame, text="Would you like to", font=("Times", 20))
label.pack(pady=5, padx=30)

create_button = customtkinter.CTkButton(master=frame, fg_color="#21866A", text="Create Account", command=lambda:create_account_section(), font=("Times", 20), width=180, height=40)
create_button.pack(pady=12, padx=10)

exit_button = customtkinter.CTkButton(master=frame, border_color="red", text="Exit", command=lambda:exit_system(), font=("Times", 20), width=180, height=35)
exit_button.pack(pady=12, padx=10)

root.mainloop()
