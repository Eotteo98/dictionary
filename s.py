import pgzrun
import random

WIDTH = 600
HEIGHT = 600

TITLE = "shoot_the_alien"
message = ""

alien2 = Actor("alien2")
alien2.pos = 0,0

def draw():
    screen.clear()
    screen.fill("white")
    alien2.draw()
    screen.draw.text(message, center = (200,20), fontsize = 25)

    
def rand():
    alien2.x = random.randint(10,WIDTH-10)
    alien2.y = random.randint(10, HEIGHT-10)

def on_mouse_down(pos):
    global message 
    if alien2.collidepoint(pos):
        message = "Good shot"
        rand()
    else:
        message = "Bad shot"
    
pgzrun.go()

