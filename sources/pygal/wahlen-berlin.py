import pygal
from pygal.style import Style
import os

myStyle = Style(
    plot_background = "#f2d98f",
    background = "#2b3e50",
    foreground = "#ffffff",
    foreground_strong = "#ffffff",
    foreground_subtle = "#2b3e50",
    colors = ("#cd0000", "#000000", "#006400", "#c71585", "#fffe00", "#1e90ff",
              "#ff7f00", "#757575", "#8b6969", "#8b4513", "#87cefa", "#ff6347",
              "#cd8500", "#8b4500")
)

wahlen = pygal.Line(show_x_guides = True, style = myStyle)
wahlen.title = "Wahlergebnisse zum Berliner Abgeordnetenhaus (1990 - 2016)"
wahlen.x_labels = map(str, [1990, 1995, 1999, 2001, 2006, 2011, 2016])
wahlen.add("SPD",        [30.4, 23.6, 22.4, 29.7, 30.8, 28.3, 21.6])
wahlen.add("CDU",        [40.4, 37.4, 40.8, 23.8, 21.3, 23.3, 17.6])
wahlen.add("Grüne",      [ 9.4, 13.2,  9.9,  9.1, 13.1, 17.6, 15.2])
wahlen.add("PDS/Linke",  [ 9.2, 14.6, 17.7, 22.6, 13.4, 11.7, 15.6])
wahlen.add("FDP",        [ 7.1,  2.5,  2.2,  9.9,  7.6,  1.8,  6.7])
wahlen.add("AfD",        [None, None, None, None, None, None, 14.2])
wahlen.add("Piraten",    [None, None, None, None, None,  8.9,  1.7])
wahlen.add("Graue",      [None,  1.7,  1.1,  1.4,  3.8, None,  1.1])
wahlen.add("REP",        [ 3.1,  2.7,  2.7,  1.3,  0.9, None, None])
wahlen.add("NPD",        [None, None,  0.8,  0.9,  2.6,  2.1,  0.6])
wahlen.add("Tierschutz", [None, None,  1.1, None,  0.8,  1.5,  1.9])
wahlen.add("Die Partei", [None, None, None, None, None,  0.9,  2.0])
wahlen.add("WASG",       [None, None, None, None,  2.9, None, None])
wahlen.add("proD",       [None, None, None, None, None,  1.2, None])

path = os.path.join(os.getcwd(), "sources/pygal/svg/wahlenberlin.svg")
wahlen.render_to_file(path)