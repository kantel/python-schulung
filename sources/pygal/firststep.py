import pygal                                                       # First import pygal
import os

bar_chart = pygal.Bar()                                            # Then create a bar graph object
bar_chart.add("Fibonacci", [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55])  # Add some values

path = os.path.join(os.getcwd(), "sources/pygal/svg/fib.svg")
bar_chart.render_to_file(path)