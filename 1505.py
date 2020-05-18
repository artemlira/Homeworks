class User:
    is_active = 'Активный'

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def __getattr__(self, attr):#возвращает атрибуты которых нет
        return attr.upper()

    def __getattribute__(self, attr):
        return attr.upper()

    def get_first_name(self):
        return self.first_name

    def set_first_name(self, first_name):
        self._first_name = first_name

    def _private(self):
        print('private')


user = User('Ivan', 'Petrov')
print(user.last_name)
print(user.is_active)
print(user.middle_name)

print(user.first_name)
print(user.get_first_name())


class Group:
    def __init__(self):
        self.__brain = 101


group = Group()
print(group.__brain)
print(group._Group__brain)
