from tkinter import *

def open_supply_window(main_window):
    supply_window = Toplevel(main_window)  # Create a new Toplevel window
    supply_window.title("Supply")
    supply_window.geometry("800x600")  # Set size for the supply window

    Label(supply_window, text="Welcome to the Supply!", font=("Times New Roman", 16)).pack(pady=20)

    # Button to close the Supply window and reopen the main window
    close_button = Button(supply_window, text="Done", command=lambda: (supply_window.destroy(), main_window.deiconify()))
    close_button.pack(pady=20)

    # Optionally, you can also handle the window close event
    supply_window.protocol("WM_DELETE_WINDOW", lambda: (supply_window.destroy(), main_window.deiconify()))