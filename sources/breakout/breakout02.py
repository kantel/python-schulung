import tkinter as tk

class World(tk.Frame):
    
    def __init__(self, master):
        super(World, self).__init__(master)
        self.width = 600
        self.height = 400
        self.canvas = tk.Canvas(self, bg = "#000000", width = self.width, height = self.height)
        self.canvas.pack()
        self.pack()

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Hello, Pong!")
    world = World(root)
    world.mainloop()