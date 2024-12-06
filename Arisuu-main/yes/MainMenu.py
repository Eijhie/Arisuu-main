from tkinter import *
from cashier import open_cashier_window
from inventory import open_inventory_window
from supply import open_supply_window

def exit_application():
    window.destroy()
    username_entry.delete(0, END)
    password_entry.delete(0, END)
    error_label.config(text="")
    login_window.deiconify()

def create_button(text, command=None):
    button = Button(window,
                    text=text,
                    font=("Times New Roman", 20),
                    fg="#1893f8",  # Set text color to #1893f8
                    bg="white",  # White background
                    state=ACTIVE,  # Keep state as ACTIVE
                    compound='bottom',
                    width=30,
                    highlightthickness=0,  # Remove highlight border
                    highlightcolor="white",  # Set highlight color to match the background
                    activebackground="white",  # Match active background to the button's background
                    activeforeground="#1893f8",  # Keep the text color the same for active state
                    command=command  # Set the command for the button
                    )
    button.pack(pady=20, padx=20)  # Use pack layout with padding

def login():
    username = username_entry.get()
    password = password_entry.get()

    if username == "admin" and password == "password":
        login_window.withdraw()
        main_window()
    else:
        error_label.config(text="Invalid username or password")

def main_window():
    global window
    window = Tk()
    window.title("Arisu Inventory System")
    window.configure(bg="#97bcc7")  # Light blue background
    window.geometry("800x600")  # Set window size to 800x600 pixels

    create_button("Cashier", lambda: (window.withdraw(), open_cashier_window(window)))
    create_button("Inventory", lambda: (window.withdraw(), open_inventory_window(window)))
    create_button("Supply", lambda: (window.withdraw(), open_supply_window(window)))
    create_button("Log Out", exit_application)

    window.mainloop()

login_window = Tk()
login_window.title("Login")
login_window.configure(bg="#97bcc7")  # Light blue background
login_window.geometry("800x600")  # Set window size to 300x200 pixels

username_label = Label(login_window, text="Username:", font=("Times New Roman", 15), bg="#97bcc7")
username_label.pack(pady=10)
username_entry = Entry(login_window, font=("Times New Roman", 15))
username_entry.pack(pady=10)

password_label = Label(login_window, text="Password:", font=("Times New Roman", 15), bg="#97bcc7")
password_label.pack(pady=10)
password_entry = Entry(login_window, font=("Times New Roman", 15), show="*")
password_entry.pack(pady=10)

error_label = Label(login_window, text="", font=("Times New Roman", 15), bg="#97bcc7", fg="red")
error_label.pack(pady=10)

login_button = Button(login_window, text="Login", font=("Times New Roman", 15), command=login)
login_button.pack(pady=10)

login_window.mainloop()