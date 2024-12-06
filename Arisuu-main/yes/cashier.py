from tkinter import *

def open_cashier_window(window):
    
    cashier_window = Toplevel(window)  # Create a new Toplevel window
    cashier_window.title("Cashier")
    cashier_window.geometry("800x600")  # Set size for the cashier window

    Label(cashier_window, text="Welcome to the Cashier!", font=("Times New Roman", 16)).pack(pady=20)

    # Button to close the Cashier window and reopen the main window
    close_button = Button(cashier_window, text="Done", command=lambda: (cashier_window.destroy(), window.deiconify()))
    close_button.pack(pady=20)

    # Optionally, you can also handle the window close event
    cashier_window.protocol("WM_DELETE_WINDOW", lambda: (cashier_window.destroy(), window.deiconify()))