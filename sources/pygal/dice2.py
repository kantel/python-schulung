import pygal
from pygal.style import LightSolarizedStyle
from die import Die
import os

die1 = Die()
die2 = Die()

results = []
for roll_num in range(1000):
    result = die1.roll() + die2.roll()
    results.append(result)

frequencies = []
max_result = die1.num_sides + die2.num_sides
for value in range(2, max_result + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

hist = pygal.Bar(style = LightSolarizedStyle)
hist.title = "Ergebnis von 1.000 Würfen zweier Würfel"
hist.x_label = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]
hist.x_title = "Augenzahl"
hist.y_title = "Häufigkeit der Augenzahlen"
hist.add("Zwei Würfel", frequencies)

path = os.path.join(os.getcwd(), "sources/pygal/svg/dice.svg")
hist.render_to_file(path)