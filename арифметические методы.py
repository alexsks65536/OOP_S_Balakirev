class Point:
    def __init__(self, x):
        self.x = x

    def __str__(self):
        return f"{self.x}"

    def __add__(self, other):
        print("__add__")
        return self.x + other

    def __radd__(self, other):
        print("__radd__")
        return other + self.x

    def __sub__(self, other):
        print("__sub__")
        return self.x - other

    def __rsub__(self, other):
        print("__rsub__")
        return other - self.x

    def __truediv__(self, other):
        print("__truediv__")
        return self.x / other


c1 = Point(10)
print(c1)
c2 = c1.x
print(c2)
c2 = c1 + 10
print(c2)
c2 = 20 + c1
print(c2)
c1 += 10
print(c1)
c2 = c1 - 4
print(c2)
c2 = 20 - c1
print(c2)
c1 = c1 / 100
print(c1)
c1 = c1 * 10
print(c1)
