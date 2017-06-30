from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk

fig = Figure(figsize = (12, 8), facecolor = "white")
axis = fig.add_subplot(211)

xValues = [1, 2, 3, 4]
yValues = [5, 7, 6, 8]
axis.plot(xValues, yValues)

axis.set_xlabel("X-Achse")
axis.set_ylabel("Y-Achse")
axis.grid()

root = tk.Tk()
root.title("MatPlotLib and Tk")

canvas = FigureCanvasTkAgg(fig, master = root)
canvas._tkcanvas.pack(side = tk.TOP, fill = tk.BOTH, expand = 1)

root.mainloop()