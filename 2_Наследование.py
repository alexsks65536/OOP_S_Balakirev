import sys

sys.path.append('d:\GB\myProject\common')
from utils import Separator

par = Separator()
par.make_separator('green', 'black', 30, '=', 'bold', 'Принципы ООП')

"""
    Создаем класс Point с атрибутами 'color', 
"""


class Point:
    """Класс для предоставления координат точек на плоскости"""
    color = 'red'  # атрибут класса
    circle = 2


a = Point()  # экземпляр класса
b = Point()
par.make_separator('yellow', 'black', 30, '=', 'bold', 'набор атрибутов класса')
print(Point.__dict__)
print(type(a) == Point)
par.make_separator('yellow', 'black', 30, '=', 'bold', 'экземпляры класса не имеют локальных атрибутов')
print(a.__dict__)
print(b.__dict__)
# Проверка принадлежности
isinstance(a, Point)
a.color = 'green'  # создание локальной переменной экземпляра класса а
par.make_separator('yellow', 'black', 30, '=', 'bold', 'экземпляры класса получил локальный атрибут')
print(a.__dict__)
print(a.color)
Point.type_pt = 'disk'  # создание новой переменной в классе Point
setattr(Point, 'prop', 1)  # создание нового атрибута prop=1 класса Point
print(Point.prop)
setattr(Point, 'type_pt', 'square')  # меняем значение атрибута type_pt класса Point
print(Point.type_pt)
res = Point.circle
print(res)
par.make_separator('yellow', 'black', 30, '=', 'bold', 'При обращении к несуществующему атрибуту - получаем False, а не error')
print(getattr(Point, 'non-existent', False))
par.make_separator('yellow', 'black', 30, '=', 'bold', 'При обращении к существующему атрибуту - получаем значение, а не False')
print(getattr(Point, 'color', False))
par.make_separator('yellow', 'black', 30, '=', 'bold', 'Удаляем атрибут класса')
print(Point.__dict__)
del Point.prop
print(Point.__dict__)
par.make_separator('yellow', 'black', 30, '=', 'bold', 'Проверяем наличие атрибута в классе')
print(hasattr(Point, 'prop'))
par.make_separator('yellow', 'black', 30, '=', 'bold', 'Удаляем атрибут класса с помощью delattr и проверяем')
delattr(Point, 'type_pt')
print(hasattr(Point, 'type_pt'))
par.make_separator('yellow', 'black', 30, '=', 'bold', 'Выводим описание класса')
print(Point.__doc__)
