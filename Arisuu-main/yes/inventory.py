from tkinter import *

def open_inventory_window(main_window):
    inventory_window = Toplevel(main_window)  # Create a new Toplevel window
    inventory_window.title("Inventory")
    inventory_window.geometry("800x600")  # Set size for the inventory window

    Label(inventory_window, text="Welcome to the Inventory!", font=("Times New Roman", 16)).pack(pady=20)

    # Button to close the Inventory window and reopen the main window
    close_button = Button(inventory_window, text="Done", command=lambda: (inventory_window.destroy(), main_window.deiconify()))
    close_button.pack(pady=20)

    # Optionally, you can also handle the window close event
    inventory_window.protocol("WM_DELETE_WINDOW", lambda: (inventory_window.destroy(), main_window.deiconify()))