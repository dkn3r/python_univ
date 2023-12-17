from config import *


class Player:
    def __init__(self, canvas, x, y, width, height, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(x, y, x + width, y + height, fill=color)
        self.vx = 0
        self.vy = 0

    def move(self):
        co = self.canvas.coords(self.id)
        if co[0] + self.vx < 0 or co[2] + self.vx > SCREEN_WIDTH:
            self.vx = 0
        if co[1] + self.vy < 0 or co[3] + self.vy > SCREEN_HEIGHT:
            self.vy = 0
        self.canvas.move(self.id, self.vx, self.vy)

    def move_up(self, event):
        self.vy = -2

    def move_down(self, event):
        self.vy = 2

    def move_left(self, event):
        self.vx = -2

    def move_right(self, event):
        self.vx = 2
    def collides_with(self,sprite):
        pos = self.canvas.coords(self.id)
        overlap = self.canvas.find_overlapping(*pos)
        return sprite.id in overlap