import timeit


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Point2D:
    __slots__ = ("x", "y")
    MAX_COORD = 100

    def __init__(self, x, y):
        self.x = x
        self.y = y


p = Point(1, 2)
p.z = 3  # Можно создать новую переменную
print(p.__dict__)
p1 = Point2D(10, 20)
p1.x = 11  # переменные можно менять, только те, которые указаны в __slots__
p1.y = 22
print(p1.x, p1.y)
# p1.z = 30  # Нельзя создать новую переменную
# print(p1.__dict__)  # в __slot__ отсутствует дополнительные имена переменных
print(p1.MAX_COORD)
