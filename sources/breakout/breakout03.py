import tkinter as tk
from gameworld03 import World

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Hello, Pong!")
    world = World(root)
    world.mainloop()