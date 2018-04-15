# Space Invaders Stage 6: Collision Detection

import turtle as t
import math

# Fenstergröße
WIDTH = 700
HEIGHT = 700
# Weltgröße
WW = 600
WH = 600

# Hier kommen die Klassendefinitionen hin

class GameWorld(t.Turtle):
    
    def __init__(self):
        t.Turtle.__init__(self)
        self.penup()
        self.hideturtle()
        self.speed(0)
        self.color("white")
        self.pensize(3)
        self.keepGoing = True
    
    def draw_border(self):
        self.penup()
        self.goto(-WW/2, -WH/2)
        self.pendown()
        for i in range(4):
            self.forward(WW)
            self.left(90)

    def exit_game(self):
        self.keepGoing = False


class Sprite(t.Turtle):
    
    def __init__(self, tshape, tcolor):
        t.Turtle.__init__(self)
        self.penup()
        self.speed(0)
        self.shape(tshape)
        self.color(tcolor)
        self.speed = 1

    def collides_with(self, obj):
        a = self.xcor() - obj.xcor()
        b = self.ycor() - obj.ycor()
        distance =  math.sqrt((a**2) + (b**2))
        if distance < 15:
            return True
        else:
            return False

class Actor(Sprite):
    
    def __init__(self, tshape, tcolor):
        Sprite.__init__(self, tshape, tcolor)
        self.color = tcolor
        self.speed = 10
        self.x = 0
        self.y = -280
        self.setheading(90)
        self.goto(self.x, self.y)
        
    def go_left(self):
        self.x -= self.speed
        if self.x <= -WW/2 + 20:
            self.x = -WW/2 + 20
        self.setx(self.x)

    def go_right(self):
        self.x += self.speed
        if self.x >= WW/2 - 20:
            self.x = WW/2 - 20
        self.setx(self.x)

class Bullet(Sprite):
    
    def __init__(self, tshape, tcolor):
        Sprite.__init__(self, tshape, tcolor)
        self.color = tcolor
        self.speed = 20
        self.setheading(90)
        self.shapesize(0.3, 0.5)
        self.state = "ready"
        self.hideturtle()
    
    def fire(self):
        if self.state == "ready":
            self.state = "fire"
            self.x = player.xcor()
            self.y = player.ycor() + 10
            self.setposition(self.x, self.y)
            self.showturtle()
        
    def move(self):
        if self.state == "fire":
            y = self.ycor()
            y += self.speed
            self.sety(y)
        if self.ycor() >= WH/2 - 20:
            self.hideturtle()
            self.state = "ready"
        if self.collides_with(enemy):
            self.hideturtle()
            self.state = "ready"
            self.setposition(-4000, -4000)
            enemy.x = -200
            enemy.y = 250
            enemy.speed = 2
            enemy.goto(enemy.x, enemy.y)


class Invader(Sprite):
    
    def __init__(self, tshape, tcolor):
        Sprite.__init__(self, tshape, tcolor)
        self.color = tcolor
        self.speed = 2
        self.x = -200
        self.y = 250
        self.goto(self.x, self.y)
    
    def move(self):
        global keepGoing
        self.x += self.speed
        if self.x >= WW/2 - 20 or self.x <= -WW/2 + 20:
            self.y -= 40
            self.sety(self.y)
            self.speed *= -1
        self.setx(self.x)
        if self.collides_with(player):
            player.hideturtle()
            self.hideturtle()
            print("Game Over!")
            # keepGoing = False

# Initialisierung

wn = t.Screen()
wn.bgcolor("#000000")
wn.setup(width = WIDTH, height = HEIGHT)
wn.title("Space Invaders – Stage 6")

# Bildschirm-Refresh ausschalten
wn.tracer(0)

# Objekte initialisieren
world = GameWorld()
world.draw_border()
player = Actor("triangle", "purple")
missile = Bullet("triangle", "yellow")
enemy = Invader("circle", "green")

# Auf Tastaturereignisse lauschen
t.listen()
t.onkey(player.go_left, "Left")
t.onkey(player.go_right, "Right")
t.onkey(missile.fire, "space")
t.onkey(world.exit_game, "Escape") # Escape beendet das Spiel

while world.keepGoing:
    wn.update()  # Bildschirm-Refresh einschalten und den gesamten Bildschirm neuzeichnen
    
    enemy.move()
    missile.move()
