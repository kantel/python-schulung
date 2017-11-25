import graphics as g
import os

WIDTH = 640
HEIGHT = 320
STEP = 32

def main():
    win = g.GraphWin("Rogue 1", WIDTH, HEIGHT)
    win.setBackground(g.color_rgb(200, 200, 200))

    path = os.path.join(os.getcwd(), "sources/graphics/images/superhero.gif")
    rogue = g.Image(g.Point(WIDTH/2-STEP/2, HEIGHT/2-STEP/2), path)
    rogue.draw(win)
    
    gameOn = True
    while gameOn:
        dx = dy = 0
        key = win.getKey()
        # print(key)
        if key == "Left":
            dx = -STEP
        elif key == "Right":
            dx = STEP
        elif key == "Up":
            dy = -STEP
        elif key == "Down":
            dy = STEP
        elif key == "Escape":
            gameOn = False
            
        print(rogue.getAnchor())
        
        if rogue.getAnchor().x = 16:
            dx = 0

        rogue.move(dx, dy)
        

if __name__ == "__main__":
    main()