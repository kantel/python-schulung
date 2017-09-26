import tkinter as tk

root = tk.Tk()
frame = tk.Frame(root)
canvas = tk.Canvas(frame, width = 600, height = 400, bg = "#000000")
frame.pack()
canvas.pack()
root.title("Hello, Pong!")
root.mainloop()