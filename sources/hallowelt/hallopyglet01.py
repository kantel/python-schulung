import pyglet as pg

window = pg.window.Window(width = 400, height = 400, caption = "Hallo PyGlet-Welt!")
image = pg.resource.image("images/python-verwirrt.jpg")
label = pg.text.Label("Hallo Jörg!", font_size = 42,
                      x = window.width//2, y = window.height//2 - 100,
                      anchor_x = "center", anchor_y = "center")

@window.event
def on_draw():
    window.clear()
    image.blit(100, 150)
    label.draw()

pg.app.run()