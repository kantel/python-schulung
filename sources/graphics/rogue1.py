import graphics as g
import os

WIDTH = 640
HEIGHT = 400


def main():
    win = g.GraphWin("Rogue 1", WIDTH, HEIGHT)
    win.setBackground(g.color_rgb(200, 200, 200))

    path = os.path.join(os.getcwd(), "sources/graphics/images/hildegund.gif")
    hildegunst = g.Image(g.Point(WIDTH/2, HEIGHT/2), path)
    hildegunst.draw(win)
    

    win.getMouse() # Pause to view result
    win.close()    # Close window when done

if __name__ == "__main__":
    main()