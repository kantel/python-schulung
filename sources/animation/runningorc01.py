import tkinter as tk
import os
import sys

root = tk.Tk()
root.title("Running Ork 01")
cycle_period = 100

def die():
    sys.exit()
    

cw, ch = 600, 100
xpos = 15
dx = 4

canvas = tk.Canvas(root, width = cw, height = ch, bg = "darkgreen")
canvas.grid(row = 0, column = 0)
path = os.path.join(os.getcwd(), "sources/animation/images/orcrt1.gif")
ork1 = tk.PhotoImage(file = path)

while True:
    xpos += dx
    canvas.create_image(xpos, ch//2, anchor = tk.CENTER, image = ork1)
    canvas.update()
    canvas.after(cycle_period)
    canvas.delete(tk.ALL)

# root.protocol("WM_DELETE_WINDOW", die)
root.mainloop()