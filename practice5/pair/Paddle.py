class Paddle:
    def __init__(self, canvas, color):
        # Зберігаємо посилання на полотно,
        # на якому буде розташована ракетка
        self.canvas = canvas
        # Створюємо прямокутний об'єкт (ракетку)
        # на полотні з заданими розмірами та кольором
        self.id = canvas.create_rectangle(0, 0, 100, 10, fill=color)
        # Переміщуємо створений прямокутник (ракетку)
        # на початкову позицію на полотні (координати 200,300)
        self.canvas.move(self.id, 200, 300)

        # Швидкість руху ракетки по горизонталі
        self.x = 0
        # Отримуємо ширину полотна для контролю руху ракетки
        # та зупинки її на краях
        self.canvas_width = self.canvas.winfo_width()
        # Прив'язуємо клавіші 'Left' та 'Right' до методів руху ракетки
        self.canvas.bind_all('<KeyPress-Left>', self.turn_left)
        self.canvas.bind_all('<KeyPress-Right>', self.turn_right)

    # Метод для руху ракетки вліво
    def turn_left(self, evt):
        self.x = -2

    # Метод для руху ракетки вправо
    def turn_right(self, evt):
        self.x = 2

    def draw(self):
        # Переміщуємо ракетку на значення x
        self.canvas.move(self.id, self.x, 0)
        # Отримуємо поточну позицію ракетки на полотні
        pos = self.canvas.coords(self.id)
        # Якщо ракетка досягла лівого краю, зупиняємо її
        if pos[0] <= 0:
            self.x = 0
        # Якщо ракетка досягла правого краю, зупиняємо її
        elif pos[2] >= self.canvas_width:
            self.x = 0

    def delete_paddle(self):
        self.canvas.delete(self.id)