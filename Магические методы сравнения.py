class Clock:
    __DAY = 86400  # Число секунд в одном дне

    def __init__(self, seconds: int):
        if not isinstance(seconds, int):
            raise TypeError("Секунды должны быть целым числом")
        self.seconds = seconds % self.__DAY

    @classmethod
    def _verify_data(cls, other):
        if not isinstance(other, (int, Clock)):
            raise TypeError("Операнд справа должен иметь тип int или Clock")

        return other if isinstance(other, int) else other.seconds

    def __eq__(self, other):
        print("Проверка на равенство __eq__")
        sc = self._verify_data(other)
        return self.seconds == sc

    def __lt__(self, other):
        print("Проверка на меньше __lt__")
        sc = self._verify_data(other)
        return self.seconds < sc

    def __gt__(self, other):
        print("Проверка на больше __lt__")
        sc = self._verify_data(other)
        return self.seconds > sc

    def __le__(self, other):
        print("Проверка на меньше или равно__lt__")
        sc = self._verify_data(other)
        return self.seconds <= sc


c1 = Clock(1000)
c2 = Clock(2000)
print(c1 == c2)
print(c1 != c2)
print(c1 < c2)
print(c1 > c2)
print(c1 <= c2)
