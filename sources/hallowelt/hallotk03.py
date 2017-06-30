import tkinter as tk
from tkinter import ttk

root = tk.Tk()

root.resizable(0, 0)
root.title("Hallo Welt!")
ttk.Label(root, text = "Hallo Jörg!").grid(column = 0, row = 0, padx = 40, pady = 40)

root.mainloop()