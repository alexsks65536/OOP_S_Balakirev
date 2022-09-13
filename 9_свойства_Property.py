class Person:
    def __init__(self, name, old):
        self.__name = name
        self.__old = old

    @property
    def old(self):
        return self.__old

    @old.setter
    def old(self, old):
        self.__old = old

    @old.deleter
    def old(self):
        del self.__old

    # old = property(get_old, set_old)
    # можно переписать в другом виде, используя декоратор "setter" и "getter"

    # old = property()
    # old = old.setter(set_old)
    # old = old.getter(get_old)


p = Person("Сергей", 20)
p.old = 35
print(p.old)
print(p.__dict__)
