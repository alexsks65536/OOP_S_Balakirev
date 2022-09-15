"""
    __МАГИЧЕСКИЕ МЕТОДЫ__
    __init__ инициализатор
    __del__ финализатор
"""


class Point:
    """Класс для предоставления координат точек на плоскости"""
    color = 'red'  # атрибут класса
    circle = 2

    def __init__(self, x=0, y=0):
        print("Вызов метода __init__")
        self.x = x
        self.y = y

    def __del__(self):  # Финализатор удаляет экземпляры класса после выполнения программы
        print("Удаление экземпляра: " + str(self))

    def set_coords(self, x, y):  # self - это ссылка на экземпляр класса
        self.x = x
        self.y = y
        print("Вызов метода set_coords" + str(self))

    def get_coords(self):
        return (self.x, self.y)


pt = Point(1, 2)
pt1 = Point()  # Если не передавать параметры, то их значения принимаются по умолчанию
print(pt.__dict__)
print(pt1.__dict__)
