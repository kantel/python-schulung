import tkinter as tk

root = tk.Tk()
root.title("Animation 01")
cw = 250            # Canvas width
ch = 130            # Canvas height

pos_x = 1
pos_y = 1
shift_x = 3
shift_y = 2
ball_width = 12
ball_height = 12
color = "red"

millisecs = 200         # 15

canvas1 = tk.Canvas(root, width = cw, height = ch, background = "white")
canvas1.grid(row = 0, column = 0)

for i in range(1, 50):
    pos_x += shift_x
    pos_y += shift_y
    canvas1.create_oval(pos_x, pos_y, pos_x + ball_width, pos_y + ball_height, fill = color)    # Create
    canvas1.update()            # Update
    canvas1.after(millisecs)    # Pause
    canvas1.delete(tk.ALL)      # Erase

print("I did it, Babe!")

root.mainloop()
