import tkinter as tk
from tkinter import ttk

root = tk.Tk()

root.resizable(0, 0)
root.title("Hallo Welt!")
labelFrame = ttk.LabelFrame(root, text = "Alles im Rahmen")
labelFrame.grid(column = 0, row = 0, padx = 20, pady = 40)
ttk.Label(labelFrame, text = "Hallo Jörg!").grid(column = 0, row = 0)

root.mainloop()