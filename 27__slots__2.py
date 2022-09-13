class Point2D:
    __slots__ = ("x", "y", "__length")

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.__length = f"Результат: {(x * x + y * y) ** 0.5}"

    @property
    def length(self):  # разрешаем атрибут класса
        return self.__length

    @length.setter
    def length(self, value):
        self.__length = value


class Point3D(Point2D):
    __slots__ = ("z",)

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


pt = Point2D(1, 2)
print(pt.length)
pt3 = Point3D(10, 20, 30)
print(pt3.x, pt3.y, pt3.z)
