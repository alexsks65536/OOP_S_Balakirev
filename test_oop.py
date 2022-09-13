class Point:
    min_coord = 0
    max_coord = 100

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_coord(self):
        print(self.x, self.y)

    def set_coord(self, x, y):
        if self.min_coord <= x <= self.max_coord:
            self.x = x
            self.y = y
        else:
            raise ValueError("!!!")

    @classmethod
    def set_bound(cls, left):
        cls.min_coord = left

    def __getattribute__(
        self, item
    ):  # вызывается при обращении к существующему атрибуту класса
        if item == "x":  # Запретить обращение к атрибуту 'x'
            print("Доступ запрещен!")
        else:
            return object.__getattribute__(self, item)

    def __setattr__(self, key, value):  # вызывается при создании атрибута класса
        if key == "z":  # Запретить создавать имя отрибута 'z'
            raise AttributeError("Недопустимое имя атрибута")
        else:
            object.__setattr__(self, key, value)

    def __getattr__(
        self, item
    ):  # вызывается при обращении к несуществующему атрибуту экземпляра класса
        return False

    def __delattr__(self, item):  # вызывается при удалении атрибута класса
        object.__delattr__(self, item)


v = Point(1, 2)
v.get_coord()
v.set_coord(10, 20)
pt1 = Point(5, 8)
# pt1.z = 0
print(v.x, v.y)
v.set_bound(-100)
print(Point.__dict__)
print(v.__dict__)
v.yy  # Обращение к несуществующему атрибуту
del v.x  # Удаление атрибута класса
print(v.__dict__)
