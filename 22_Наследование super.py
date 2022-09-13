class Geom:
    name = "Geom"

    def __init__(self, x1, y1, x2, y2):
        print(f"инициализатор Geom для {self.__class__}")
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2


class Line(Geom):
    def draw(self):
        print("Рисование линии")


class Rect(Geom):
    def __init__(self, x1, y1, x2, y2, fill=None):  # добавили параметр "Заливка"
        super().__init__(
            x1,
            y1,
            x2,
            y2,
        )  # вызов родительского класса "Geom" - делегирование
        self.fill = fill

    def draw(self):
        print("Рисование прямоугольника")


l = Line(0, 0, 10, 2)
r = Rect(1, 1, 4, 4, 10)
print(l.__dict__)
print(r.__dict__)
