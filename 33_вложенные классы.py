class Women:
    title = "объект класса для поля title"
    photo = "объект класса для поля photo"
    ordering = "объект класса для поля ordering"

    def __init__(self, user, psw):
        self.user = user
        self.psw = psw
        self.meta = self.Meta(user + '@' + psw)

    class Meta:
        ordering = ['id']

        def __init__(self, access):
            self._access = access


# print(Women.ordering)
# print(Women.Meta.ordering)

w = Women('root', '12345')
print(w.__dict__)
print(w.meta.__dict__)