import tkinter as tk

root = tk.Tk()
root.title("Animation 02")
cw = 250            # Canvas width
ch = 250            # Canvas height

pos_x1 = 1
pos_y1 = 1
shift_x1 = 1
shift_y1 = 1
ball1_width = 16
ball1_height = 16
color1 = "red"

pos_x2 = 180
pos_y2 = 180
shift_x2 = -2
shift_y2 = -2
ball2_width = 12
ball2_height = 12
color2 = "blue"


millisecs = 100         # 15

canvas1 = tk.Canvas(root, width = cw, height = ch, background = "black")
canvas1.grid(row = 0, column = 0)

for i in range(1, 50):
    pos_x1 += shift_x1
    pos_y1 += shift_y1
    pos_x2 += shift_x2
    pos_y2 += shift_y2

    canvas1.create_oval(pos_x1, pos_y1, pos_x1 + ball1_width, pos_y1 + ball1_height, fill = color1)    # Create
    canvas1.create_oval(pos_x2, pos_y2, pos_x2 + ball2_width, pos_y2 + ball2_height, fill = color2)
    canvas1.update()            # Update
    canvas1.after(millisecs)    # Pause
    canvas1.delete(tk.ALL)      # Erase

print("I did it, Babe!")

root.mainloop()
