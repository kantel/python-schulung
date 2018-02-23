import turtle as t

wn = t.Screen()
wn.colormode(255)
wn.bgcolor(43, 62, 80)
wn.setup(width = 600, height = 600)
wn.title("Ein Sieben-Eck")

alex = t.Turtle()
alex.pensize(2)
alex.pencolor("red")

def polygon(t, n, length):
    angle = 360.0/n
    for i in range(n):
        t.forward(length)
        t.left(angle)
    
polygon(alex, 7, 70)

wn.mainloop()