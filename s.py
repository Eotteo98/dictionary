import pgzrun
import random

WIDTH = 600
HEIGHT = 600

TITLE = "shoot_the_alien"
message = ""

alien = Actor("alien")
alien.pos = 0,0

def draw():
    screen.clear()
    screen.fill("black")
    alien.draw()
    screen.draw.text(message, center = (200,20), fontsize = 25)

    
def rand():
    alien.x = random.randint(10,WIDTH-10)
    alien.y = random.randint(10, HEIGHT-10)

def on_mouse_down(pos):
    global message 
    if alien.collidepoint(pos):
        message = "Good shot"
        rand()
    else:
        message = "Bad shot"
    
pgzrun.go()

