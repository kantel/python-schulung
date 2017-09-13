from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk

fig = Figure(figsize = (12, 8), facecolor = "white")

axis1 = fig.add_subplot(211)

xValues = [1, 2, 3, 4]
yValues1 = [5, 7, 6, 8]
axis1.plot(xValues, yValues1)

axis1.set_xlabel("X-Achse")
axis1.set_ylabel("Y-Achse")
axis1.grid(linestyle = "-")

axis2 = fig.add_subplot(212)

yValues2 = [7, 5, 8, 6]
axis2.plot(xValues, yValues2)
axis2.grid()

root = tk.Tk()
root.title("MatPlotLib and Tk (2)")

canvas = FigureCanvasTkAgg(fig, master = root)
canvas._tkcanvas.pack(side = tk.TOP, fill = tk.BOTH, expand = 1)

root.mainloop()
