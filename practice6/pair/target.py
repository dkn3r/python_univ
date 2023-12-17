from config import *


class Target:
    def __init__(self, canvas, radius, color):
        self.canvas = canvas
        self.x = random.randint(radius, SCREEN_WIDTH - radius)
        self.y = random.randint(radius, SCREEN_HEIGHT - radius)
        self.radius = radius
        self.id = canvas.create_oval(self.x-radius,self.y-radius,self.x+radius,self.y+radius,fill=color)
