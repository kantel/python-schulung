import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()
root.title("Hallöchen, Du verwirrte Schlange")

cw, ch = 400, 400
canvas = tk.Canvas(root, width = cw, height = ch, bg = "royalblue")
canvas.grid(row = 0, column = 0)

image = Image.open("/Users/admin/git/python-schulung/sources/tkgraphics/images/python-verwirrt.png")
schlange = ImageTk.PhotoImage(image)
canvas.create_image(cw//2, ch//2, anchor = tk.CENTER, image = schlange)
canvas.update

root.mainloop()