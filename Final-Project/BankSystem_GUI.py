import customtkinter
import os
from PIL import Image
from tkinter import messagebox
from tkinter import Toplevel

customtkinter.set_appearance_mode("black")
customtkinter.set_default_color_theme("green")

def main_menu():
    main_menu_window = customtkinter.CTk()
    main_menu_window.geometry("600x400")
    main_menu_window.mainloop()

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
    create_window.geometry("400x260")
    create_window.title("Create Account")
    root.withdraw()

    frame_create = customtkinter.CTkFrame(master=create_window)
    frame_create.pack(pady=30, padx=30, fill="both", expand=False)

    label_create = customtkinter.CTkLabel(master=frame_create, text="Create an account", font=("Times", 20))
    label_create.pack(pady=12, padx=10)

    username_create = customtkinter.CTkEntry(master=frame_create, placeholder_text="Username", font=("Times", 14))
    username_create.pack(pady=12, padx=10)

    password_create = customtkinter.CTkEntry(master=frame_create, placeholder_text="Password", show="*", font=("Times", 14))
    password_create.pack(pady=12, padx=10)

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

    create_button = customtkinter.CTkButton(master=frame_create, border_color="red", text="Create Account", command=create_account, font=("Times", 14))
    create_button.pack(pady=12, padx=10)
    create_window.bind("<Return>", lambda event=None: create_account())

def login_account_section():
    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("green")
    login_window = Toplevel(root)
    login_window.geometry("400x260")
    login_window.title("Login")

    frame_login = customtkinter.CTkFrame(master=login_window)
    frame_login.pack(pady=30, padx=30, fill="both", expand=False)

    label_login = customtkinter.CTkLabel(master=frame_login, text="Login", font=("Times", 20))
    label_login.pack(pady=12, padx=10)

    username_login = customtkinter.CTkEntry(master=frame_login, placeholder_text="Username", font=("Times", 14))
    username_login.pack(pady=12, padx=10)

    password_login = customtkinter.CTkEntry(master=frame_login, placeholder_text="Password", show="*", font=("Times", 14))
    password_login.pack(pady=12, padx=10)

    def login_attempt():
        entered_username = username_login.get()
        entered_password = password_login.get()

        if created_username == entered_username and created_password == entered_password:
            messagebox.showinfo("Login Successful", "Welcome to the Doynamic Bank!")
            login_window.destroy()  # Close the login window
            main_menu()
        else:
            messagebox.showerror("Login Failed", "Please check your credentials.")

    login_button = customtkinter.CTkButton(master=frame_login, border_color="red", text="Login", command=login_attempt, font=("Times", 14))
    login_button.pack(pady=12, padx=10)

    # Bind the Enter key to the login button
    login_window.bind("<Return>", lambda event=None: login_attempt())

root = customtkinter.CTk()
root.geometry("400x260")
root.title("Welcome to Doynamic Bank!")

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=30, padx=30, expand=True)

label = customtkinter.CTkLabel(master=frame, text="Doynamic Bank", font=("Times", 42))
label.pack(pady=12, padx=30)


label = customtkinter.CTkLabel(master=frame, text="Would you like to", font=("Times", 20))
label.pack(pady=5, padx=30)

# Create Account Section
create_button = customtkinter.CTkButton(master=frame, border_color="red", text="Create Account", command=lambda:create_account_section(), font=("Times", 20))
create_button.pack(pady=12, padx=10)

root.mainloop()
