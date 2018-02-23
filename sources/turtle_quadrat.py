import turtle as t

wn = t.Screen()
wn.colormode(255)
wn.bgcolor(43, 62, 80)
wn.setup(width = 600, height = 600)
wn.title("Ein Quadrat")

alex = t.Turtle()
alex.pensize(2)
alex.pencolor("red")

def quadrat(t):
    for i in range(4):
        t.forward(100)
        t.left(90)

quadrat(alex)

berta = t.Turtle()
berta.pensize(2)
berta.pencolor("white")

berta.goto(-100, 0)

quadrat(berta)

wn.mainloop()