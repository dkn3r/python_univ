import random

from app import *


# Клас PlatformSprite представляє платформи у грі та є нащадком класу Sprite.
class PlatformSprite(Sprite):
    # Ініціалізація платформи.
    def __init__(self, game, photo_image, x, y, width, height):
        self.game = game
        self.width = width
        self.height = height
        # Викликаємо ініціалізатор батьківського класу Sprite.
        Sprite.__init__(self, game)
        # Зберігаємо зображення платформи.
        self.photo_image = photo_image
        # Створюємо зображення платформи на ігровому полотні.
        self.image = game.canvas.create_image(x, y, image=self.photo_image,
                                              anchor='nw')
        self.speed = random.randint(-2, 2)
        # Встановлюємо координати платформи.
        self.coordinates = Coords(x, y, x + width, y + height)
        # Створюємо червоний контур навколо платформи для наочності
        # (Використовуємо для налагодження).
        # self.border = game.canvas.create_rectangle(x, y, x + width, y + height, outline="red")

    def move(self):
        self.game.canvas.move(self.image, self.speed, 0)
        x, y = self.game.canvas.coords(self.image)

        if x + self.speed <= 0 or x + self.width + self.speed >= self.game.canvas_width:
            self.speed = -self.speed
        self.coordinates = Coords(x, y, x + self.width, y + self.height)
