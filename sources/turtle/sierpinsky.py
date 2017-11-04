# Sierpinksy-Dreieck mit der Turtlegraphik

import turtle as t

l = 400

wn = t.Screen()
wn.bgcolor("black")
wn.setup(width = 600, height = 400)
wn.title("Sierpinsky-Dreieck")

sierp = t.Turtle()
sierp.pencolor("white")
sierp.pensize(2)

def sierpinsky(l):
    if l > 20:
        for i in range(3):
            sierpinsky(l/2)
            sierp.forward(l)
            sierp.right(120)

sierp.penup()
sierp.goto(-200, 180)
sierp.pendown()
sierpinsky(l)

wn.mainloop()