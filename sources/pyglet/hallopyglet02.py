import pyglet as pg

window = pg.window.Window(width = 400, height = 400, caption = "Hallo PyGlet-Welt!")
r, g, b, alpha = 0.5, 0.5, 0.8, 0.5
pg.gl.glClearColor(r, g, b, alpha)
image = pg.resource.image("images/python-verwirrt.png")
label = pg.text.Label("Hallo Joerg!", font_size = 42,
                      x = window.width//2, y = window.height//2 - 100,
                      anchor_x = "center", anchor_y = "center")

@window.event
def on_draw():
    window.clear()
    image.blit(100, 150)
    label.draw()

pg.app.run()
