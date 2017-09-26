import tkinter as tk
from gameworld05 import World

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Break Out!")
    world = World(root)
    world.mainloop()