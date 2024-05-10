import tkinter as tk
from tkinter import Label, Button

def create_window(password:str) ->bool:
    root = tk.Tk()
    root.title("password generator")
    root.geometry("400x350")

    Label(root, text=password).pack(padx = 30, pady = 30)

    root.mainloop()
    return True