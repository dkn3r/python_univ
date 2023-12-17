from CollisionCheck import CollisionCheck
from app import *

# Клас, який представляє спрайт дверей у грі
class DoorSprite(Sprite):
    def __init__(self, game, photo_image_closed, photo_image_open, x, y, width, height):
        super().__init__(game)

        self.photo_image_closed = photo_image_closed
        self.photo_image_open = photo_image_open

        self.image = game.canvas.create_image(x, y, image=self.photo_image_closed, anchor='nw')

        self.coordinates = Coords(x, y, x + (width / 2), y + height)
        self.endgame = True
        self.opened = False  # Додано атрибут для відстеження стану дверей

    def open_door(self):
        if not self.opened:
            self.game.canvas.itemconfig(self.image, image=self.photo_image_open)
            self.opened = True

    def close_door(self):
        if self.opened:
            self.game.canvas.itemconfig(self.image, image=self.photo_image_closed)
            self.opened = False