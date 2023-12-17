class Coords:
    # Конструктор класу. Ініціалізує об'єкт із заданими координатами.
    # Якщо координати не задані, вони ініціалізуються нулями.
    def __init__(self, x1=0, y1=0, x2=0, y2=0):
        self.x1 = x1  # Координата x лівого верхнього кута
        self.y1 = y1  # Координата y лівого верхнього кута
        self.x2 = x2  # Координата x правого нижнього кута
        self.y2 = y2  # Координата y правого нижнього кута

    def overlapping(self, other_coords):
        return not (self.x2 < other_coords.x1 or
                    self.x1 > other_coords.x2 or
                    self.y2 < other_coords.y1 or
                    self.y1 > other_coords.y2)