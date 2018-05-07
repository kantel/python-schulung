# Hallo Canvas!

import tkinter as tk

cw = 400        # Canvas width
ch = 100        # Canvas height

root = tk.Tk()
root.title("Hallo Welt!")

my_canvas = tk.Canvas(root, width = cw, height = ch, background = "white")
my_canvas.grid(column = 0, row = 0)

xy = cw//2, ch//2
my_canvas.create_text(xy, text = "Hallo Wörld!")

root.mainloop()