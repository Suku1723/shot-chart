import customtkinter as ctk
from tkinter import *
from tkcalendar import Calendar
from test import DailyGames

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

root = ctk.CTk()

root.title('Tkinter.com - Custom Tkinter Date Picker')
root.geometry('600x450')

# Global list to keep track of created buttons
created_buttons = []

def clear_screen():
    global created_buttons
    # Destroy all buttons in the created_buttons list
    for button in created_buttons:
        button.destroy()
    # Clear the list
    created_buttons.clear()

def pick_date():
    def on_date_selected(event):
        global created_buttons

        # Clear the screen before adding new buttons
        clear_screen()

        DG = DailyGames(cal.selection_get().year, cal.selection_get().month, cal.selection_get().day)
        games_list = DG.get_dummy_data()

        for i in range(len(games_list)):
            button = ctk.CTkButton(root, text=f"{games_list[i]}", fg_color="red", hover_color="maroon")
            button.pack(pady=20)
            created_buttons.append(button)  # Store reference to new button
        
        top.destroy()
    
    top = ctk.CTkToplevel(root)
    top.title('Select a Date')
    cal = Calendar(top, selectmode='day', year=2024, month=7, day=1)
    cal.pack(pady=20)
    cal.bind("<<CalendarSelected>>", on_date_selected)

my_button = ctk.CTkButton(root, text="Pick a Date", command=pick_date)
my_button.pack(pady=20)

x_scrollbar = ctk.CTkScrollbar(root, orientation='horizontal')
x_scrollbar.pack(side=ctk.BOTTOM, fill=ctk.X)

y_scrollbar = ctk.CTkScrollbar(root, orientation='vertical')
y_scrollbar.pack(side=ctk.RIGHT, fill=ctk.Y)

root.mainloop()