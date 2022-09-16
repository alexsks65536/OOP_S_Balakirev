class Master:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def instancemethod(self):
        return print(f"Работает метод экземпляра класса: {self.x}, {self.y}, {self}")

    @classmethod
    def class_method(cls, x, y):
        return print(f"Работает класс метод: {x}, {y}, {cls}")

    @staticmethod
    def static_method(x, y):
        return print(f"Работает статик метод: {x}, {y}")


class Date:
    def __init__(self, day=0, month=0, year=0):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def from_string(cls, date_as_string):
        day, month, year = map(int, date_as_string.split('.'))
        date1 = cls(day, month, year)
        return date1

    def string_to_db(self):
        return print(f'{self.year}-{self.month}-{self.day}')


m = Master(1, 2)
m.instancemethod()
# Master.instancemethod()  так не работает
print("=" * 30)
m.class_method(1, 2)
Master.class_method(1, 2)  # а так работает
print("=" * 30)
m.static_method(1, 2)
Master.static_method(1, 2)  # и так работает
print("=" * 50)
# =====================================================
string_date = '10.10.2020'
day, month, year = map(int, string_date.split('.'))
date = Date(day, month, year)
date.string_to_db()
print("=" * 30)
date1 = Date.from_string('30.12.2020')
date1.string_to_db()
date2 = Date.from_string('01.01.2021')
date2.string_to_db()
