import random


class Ball:
    def __init__(self, canvas, paddle, color):

        self.canvas = canvas
        self.paddle = paddle
        self.score = 0
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
        self.canvas.move(self.id, 245, 100)

        # Створюємо список можливих стартових значень для руху м'яча по осі X
        starts = [-3, -2, -1, 1, 2, 3]
        # Випадковим чином перетасовуємо список
        random.shuffle(starts)
        # Беремо перший елемент зі списку як стартове значення для руху м'яча по осі X
        self.x = starts[0]
        # Задаємо стартову швидкість руху м'яча по осі Y
        self.y = -1
        # Отримуємо висоту та ширину полотна для визначення меж руху м'яча
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()

        # Властивість для визначення, чи доторкнувся м'яч до нижньої частини полотна
        self.hit_bottom = False
        self.score = 0
        self.score_text = self.canvas.create_text(450, 10, text="Score: 0")

    # Метод для визначення зіткнення м'яча з ракеткою
    def hit_paddle(self, pos):
        paddle_pos = self.canvas.coords(self.paddle.id)
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if paddle_pos[1] <= pos[3] <= paddle_pos[3]:
                distance_from_center = (pos[2] - paddle_pos[0]) - (paddle_pos[2] - pos[2])
                self.x = distance_from_center / 10
                self.score += 1
                self.canvas.itemconfig(self.score_text, text=f"Score: {self.score}")
                return True
        return False



    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        # Якщо нижня частина м'яча досягла верхньої частини полотна
        if (pos[0] <= 0 and self.x < 0) or (pos[2] >= self.canvas_width and self.x > 0):
            self.x = -self.x
            # Якщо м'яч вдарив верхню стіну, відбиваємо його вниз
        if pos[1] <= 0:
            self.y = 1
            # Якщо м'яч вдарив нижню стіну, зупиняємо гру
        if pos[3] >= self.canvas_height:
            self.hit_bottom = True
            # Якщо м'яч зіткнувся з ракеткою
        if self.hit_paddle(pos):
            self.y = -1
        return

    def delete_ball(self):
        self.canvas.delete(self.id)

    def start_score(self):
        self.score = 0
        self.canvas.itemconfig(self.score_text, text=f"Score: {self.score}")
        self.canvas.delete(self.score_text)


