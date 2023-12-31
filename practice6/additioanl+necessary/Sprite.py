# Клас Sprite представляє основний шаблон для всіх ігрових об'єктів.
class Sprite:
    # Ініціалізація спрайта.
    def __init__(self, game):
        # Зберігаємо посилання на основний ігровий об'єкт.
        self.game = game
        # Змінна, яка вказує, чи завершилася гра.
        self.endgame = False
        # Змінна для зберігання координат спрайта.
        self.coordinates = None

    # Функція для переміщення спрайта (буде перевизначена у дочірніх класах).
    def move(self):
        pass

    # Функція, яка повертає поточні координати спрайта.
    def coords(self):
        return self.coordinates

    