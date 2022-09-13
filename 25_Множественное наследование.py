class Goods:
    """Базовый класс описания товара"""
    def __init__(self, name, weight, price):
        super().__init__()  # Запуск инициализатора класс MixinLog
        print("init Goods")
        self.name = name
        self.weight = weight
        self.price = price

    def print_info(self):
        print(f"{self.name} {self.weight} {self.price}")


class MixinLog:
    """Независимый базовый класс"""
    ID = 0

    def __init__(self):
        print("init MixinLog")
        self.ID += 1
        self.id = self.ID

    def save_sell_log(self):
        print(f"{self.id}: товар был продан в 00:00 часов")

    def print_info(self):
        print("print_info из MixinLog")


class MixinLog2:
    def __init__(self):
        super().__init__()
        print("MixinLog2")


class Notebook(Goods, MixinLog, MixinLog2):
    def print_info(self):
        MixinLog.print_info(self)


n = Notebook("Acer", 1.5, 30000)
n.print_info()
n.save_sell_log()
print(Notebook.__mro__)  # выводится список классов при поиске атрибута
