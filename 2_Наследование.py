from .myProject.common.utils import Separator

par = Separator()
par.make_separator('yellow', 'black', 100, '$', 'bold')


class Point:
    color = 'red'  # атрибут класса
    circle = 2


a = Point()  #  экземпляр класса
b = Point()
print(Point.__dict__)
print(type(a) == Point)
print(a.__dict__)
print(b.__dict__)
# Проверка принадлежности
isinstance(a, Point)
a.color = 'green'  # создание локальной переменной экземпляра класса а
print(a.__dict__)
print(a.color)
Point.type_pt = 'disk'  # создание новой переменной в классе Point
setattr(Point, 'prop', 1)  # создание нового атрибута prop=1 класса Point
print(Point.prop)
setattr(Point, 'type_pt', 'square')  # меняем значение атрибута type_pt класса Point
print(Point.type_pt)
res = Point.circle
print(res)
print('=' * 20)
print(getattr(Point, 'non-existent', False))  # При обращении к несуществующему атрибуту - получаем False, а не error
print(getattr(Point, 'color', False))  # При обращении к существующему атрибуту - получаем значение, а не False
