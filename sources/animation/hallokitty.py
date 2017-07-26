import tkinter as tk
import os

root = tk.Tk()
root.title("Hallo Kitty")

cw, ch = 400, 400
canvas = tk.Canvas(root, width = cw, height = ch, bg = "darkgreen")
canvas.grid(row = 0, column = 0)

path = os.path.join(os.getcwd(), "sources/animation/images/horngirl.gif")
print(os.getcwd())
horngirl = tk.PhotoImage(file = path)
canvas.create_image(cw//2, ch//2, anchor = tk.CENTER, image = horngirl)
canvas.update()

root.mainloop()