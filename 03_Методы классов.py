class Point:
    """Класс для предоставления координат точек на плоскости"""
    color = 'red'  # атрибут класса
    circle = 2

    def set_coords(self, x, y):  # self - это ссылка на экземпляр класса
        self.x = x
        self.y = y
        print("Вызов метода set_coords" + str(self))

    def get_coords(self):
        return (self.x, self.y)


print(Point.set_coords)
# print(Point.set_coords())
pt = Point()
pt2 = Point()
print(pt.set_coords)
pt.set_coords(1, 2)
pt2.set_coords(10, 20)
print(pt.__dict__)
print(pt2.__dict__)
print(pt.get_coords())
print(pt2.get_coords())
f = getattr(pt, 'get_coords')  # Это редко применяется
print(f)
print(f())