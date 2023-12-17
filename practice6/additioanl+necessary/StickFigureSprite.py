from CollisionCheck import CollisionCheck
from app import *
from DoorSprite import DoorSprite


# Клас StickFigureSprite представляє спрайт (графічний об'єкт) чоловічка в грі та є нащадком класу Sprite.
class StickFigureSprite(Sprite):
    # Ініціалізатор для класу StickFigureSprite
    def __init__(self, game):
        # Отримуємо доступ до холста гри
        self.canvas = game.canvas

        # Ініціалізація батьківського класу Sprite
        Sprite.__init__(self, game)

        # Завантажуємо зображення чоловічка, який дивиться вліво
        self.images_left = [
            PhotoImage(file="img/figure-L1.png"),
            PhotoImage(file="img/figure-L2.png"),
            PhotoImage(file="img/figure-L3.png")
        ]

        # Завантажуємо зображення чоловічка, який дивиться вправо
        self.images_right = [
            PhotoImage(file="img/figure-R1.png"),
            PhotoImage(file="img/figure-R2.png"),
            PhotoImage(file="img/figure-R3.png")
        ]

        # Встановлюємо початкове зображення чоловічка на холсті
        self.image = game.canvas.create_image(200, 370, image=self.images_left[0], anchor='nw')

        # Налаштовування початкових параметрів для чоловічка
        self.x = -2  # Початковий горизонтальний рух
        self.y = 2  # Початковий вертикальний рух (0 означає, що не в русі)
        self.current_image = 0  # Поточне зображення
        self.current_image_add = 1  # Інкремент для зміни зображення
        self.jump_count = 0  # Лічильник стрибків
        self.last_time = time.time()  # Час останньої анімації
        self.coordinates = Coords()  # Об'єкт координат

        # Прив'язка дій до клавіш
        game.canvas.bind_all('<KeyPress-Left>', self.turn_left)  # Рух вліво
        game.canvas.bind_all('<KeyPress-Right>', self.turn_right)  # Рух вправо
        game.canvas.bind_all('<space>', self.jump)  # Стрибок
        game.canvas.bind_all('<Escape>', self.on_escape)  # Вихід з гри

    # Функція вихід з гри при натисненні Escape
    def on_escape(self, event=None):
        if not self.game.start_time:
            self.game.start_timer()
        self.game.canvas.destroy()  # Знищення холста
        self.game.game_over = True  # Встановлення стану гри як завершена
        self.game.stop()  # Зупинка гри
        print("Гра завершена!")  # Виведення повідомлення

    # Функція руху вліво
    def turn_left(self, evt):
        if self.y == 0:  # Якщо чоловічок не у вертикальному русі
            self.x = -2  # Встановлення напрямку руху вліво
            self.game.start_timer()

    # Функція руху вправо
    def turn_right(self, evt):
        if self.y == 0:  # Якщо чоловічок не у вертикальному русі
            self.x = 2  # Встановлення напрямку руху вправо
            self.game.start_timer()

    # Функція стрибка
    def jump(self, evt):
        if self.y == 0:  # Якщо чоловічок не у вертикальному русі
            self.y = -4  # Задання напрямку стрибка вгору
            self.jump_count = 0  # Скидання лічильника стрибків
            self.game.start_timer()

    # Додаємо мето д animate до класу StickFigureSprite для анімації фігурки
    def animate(self):
        # Якщо фігурка рухається горизонтально і не у вертикальному русі (не стрибає)
        if self.x != 0 and self.y == 0:
            # Якщо пройшло більше ніж 0.1 секунди від останньої анімації
            if time.time() - self.last_time > 0.1:
                # Оновлюємо час останньої анімації
                self.last_time = time.time()
                # Змінюємо поточне зображення на наступне/попереднє
                self.current_image += self.current_image_add
                # Якщо досягли останнього зображення, змінюємо напрямок анімації
                if self.current_image >= 2:
                    self.current_image_add = -1
                # Якщо досягли першого зображення, змінюємо напрямок анімації
                if self.current_image <= 0:
                    self.current_image_add = 1

        # Якщо фігурка рухається вліво
        if self.x < 0:
            # Якщо фігурка стрибає, показуємо третє зображення вліво
            if self.y != 0:
                self.game.canvas.itemconfig(self.image, image=self.images_left[2])
            # Інакше показуємо поточне зображення анімації вліво
            else:
                self.game.canvas.itemconfig(self.image, image=self.images_left[self.current_image])
        # Якщо фігурка рухається вправо
        elif self.x > 0:
            # Якщо фігурка стрибає, показуємо третє зображення вправо
            if self.y != 0:
                self.game.canvas.itemconfig(self.image, image=self.images_right[2])
            # Інакше показуємо поточне зображення анімації вправо
            else:
                self.game.canvas.itemconfig(self.image, image=self.images_right[self.current_image])

    def coords(self):
        # Отримання координат фігурки на холсті за допомогою методу coords
        xy = self.game.canvas.coords(self.image)

        # Встановлення x1 та y1 для координат фігурки
        self.coordinates.x1 = xy[0]
        self.coordinates.y1 = xy[1]

        # Встановлення x2 та y2, враховуючи розміри фігурки (27x30 пікселів)
        self.coordinates.x2 = xy[0] + 27
        self.coordinates.y2 = xy[1] + 30

        print(xy)
        # Повернення об'єкту координат для подальшого використання
        return self.coordinates

    def move(self):
        # Виклик методу для анімації фігурки
        self.animate()

        # Умови для контролю стрибка фігурки. Якщо фігурка стрибає вгору:
        if self.y < 0:
            self.jump_count += 1
            # Якщо фігурка стрибає довше, ніж 20 кадрів, почніть падіння
            if self.jump_count > 20:
                self.y = 4

        # Якщо фігурка падає вниз, зменшуйте лічильник стрибка
        if self.y > 0:
            self.jump_count -= 1

        # Отримання поточного положення фігурки на холсті
        co = self.coords()

        # Ініціалізація змінних, які контролюють можливі зіткнення фігурки
        left = True
        right = True
        top = True
        bottom = True
        falling = True

        # Перевірка на зіткнення фігурки з нижньою межею холста
        if self.y > 0 and co.y2 >= self.game.canvas_height:
            self.y = 0
            bottom = False

        # Перевірка на зіткнення фігурки з верхньою межею холста
        elif self.y < 0 and co.y1 <= 0:
            self.y = 0
            top = False

        # Перевірка на зіткнення фігурки з правою межею холста
        if self.x > 0 and co.x2 >= self.game.canvas_width:
            self.x = 0
            right = False

        # Перевірка на зіткнення фігурки з лівою межею холста
        elif self.x < 0 and co.x1 < 0:
            self.x = 0
            left = False
        # Перевірка зіткнення чоловічка з іншими спрайтами в грі
        for sprite in self.game.sprites:
            # Пропустити спрайт, якщо він є самим чоловічком
            if sprite == self:
                continue

            # Отримання координат поточного спрайта
            sprite_co = sprite.coords()

            # Обробка зіткнення зверху
            if top and self.y < 0 and CollisionCheck.collided_top(co, sprite_co):
                self.y = -self.y
                top = False

            # Обробка зіткнення знизу
            if bottom and self.y > 0 and CollisionCheck.collided_bottom(self.y, co, sprite_co):
                self.y = 0
                bottom = False
                top = False

            # Перевірка, чи потрібно зупинити падіння фігурки, якщо вона зіткнулася з іншим спрайтом знизу
            if bottom and falling and self.y == 0 and co.y2 < self.game.canvas_height and CollisionCheck.collided_bottom(
                    1, co,
                    sprite_co):
                falling = False

            # Обробка зіткнення зліва
            if left and self.x < 0 and CollisionCheck.collided_left(co, sprite_co):
                self.x = 0
                left = False

                # Завершення гри, якщо спрайт має властивість endgame
                if sprite.endgame:
                    self.game.game_over = True
                    # Код для відображення повідомлення про завершення гри (відключено)
                    self.game.canvas.create_text(250, 250, text="Ви перемогли!", font=('Arial', 30), fill='green')

            # Обробка зіткнення справа
            if right and self.x > 0 and CollisionCheck.collided_right(co, sprite_co):
                self.x = 0
                right = False

                # Завершення гри, якщо спрайт має властивість endgame
                if sprite.endgame:
                    self.game.game_over = True
            if isinstance(sprite, DoorSprite) and self.coords().overlapping(sprite.coordinates):
                sprite.open_door()
                self.game.canvas.after(300, sprite.close_door)
                self.game.canvas.after(300, self.hide_character)
                self.game.start_time = None
                self.game.stop_timer()
        # Якщо фігурка все ще падає і не зіткнулася з іншим спрайтом, дайте їй рухатися вниз
        if falling and bottom and self.y == 0 and co.y2 < self.game.canvas_height:
            self.y = 4

        # Рух фігурки на холсті на відповідну відстань по осі x та y
        self.game.canvas.move(self.image, self.x, self.y)

    def hide_character(self):
        self.game.canvas.itemconfig(self.image, state='hidden')
