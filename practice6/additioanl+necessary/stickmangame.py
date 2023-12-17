from app import *


g = Game()

# Отримуємо доступ до холста гри,
# на якому будуть відображатися об'єкти.
canvas = g.canvas

platform1 = PlatformSprite(g, PhotoImage(file="img/platform1.png"),
                           0, 460, 100, 10)
platform2 = PlatformSprite(g, PhotoImage(file="img/platform1.png"),
                           250, 400, 100, 10)
platform3 = PlatformSprite(g, PhotoImage(file="img/platform1.png"),
                           100, 340, 100, 10)
platform4 = PlatformSprite(g, PhotoImage(file="img/platform1.png"),
                           0, 280, 100, 10)
platform5 = PlatformSprite(g, PhotoImage(file="img/platform1.png"),
                           250, 220, 100, 10)
platform6 = PlatformSprite(g, PhotoImage(file="img/platform1.png"),
                           100, 160, 100, 10)
platform7 = PlatformSprite(g, PhotoImage(file="img/platform1.png"),
                           0, 100, 100, 10)
platform8 = PlatformSprite(g, PhotoImage(file="img/platform1.png"),
                           250, 40, 100, 10)
platform9 = PlatformSprite(g, PhotoImage(file="img/platform1.png"),
                           200, 280, 100, 10)
platform10 = PlatformSprite(g, PhotoImage(file="img/platform1.png"),
                            230, 100, 100, 10)
platform11 = PlatformSprite(g, PhotoImage(file="img/platform1.png"),
                            200, 460, 100, 10)


g.sprites.append(platform1)
g.sprites.append(platform2)
g.sprites.append(platform3)
g.sprites.append(platform4)
g.sprites.append(platform5)
g.sprites.append(platform6)
g.sprites.append(platform7)
g.sprites.append(platform8)
g.sprites.append(platform9)
g.sprites.append(platform10)
g.sprites.append(platform11)

# Створення спрайта дверей із вказаним зображенням
# та заданими координатами та розмірами
closed_door = PhotoImage(file="img/door1.png")
opened_door = PhotoImage(file="img/door2.png")
door = DoorSprite(g, closed_door, opened_door,
                  45, 40, 40, 35)

# Додавання спрайта дверей до гри
g.sprites.append(door)

# Створення нового спрайта - чоловічка,
# базуючись на класі StickFigureSprite
# і передаємо об'єкт гри (g) як параметр
sf = StickFigureSprite(g)

# Додавання створеного спрайта чоловічка
# до списку спрайтів в об'єкті гри
g.sprites.append(sf)

# Запуск головного циклу гри
g.mainloop()


g.root.mainloop()
