class User:
    is_active = True
    is_blocket = False

    def __new__(cls, *args, **kwargs):
        print('its NEW')
        return super(User, cls).__new__(cls)

    def __init__(self, name):
        print('its INIT')
        self.name = name

    def __del__(self):
        print(f'удалили объект {self.name}')

    def set_block(self):
        self.is_blocket = True

    @staticmethod
    def say_hi():
        print('hi')

    @classmethod
    def say_hello(cls, x):
        print(f'Hello, I`m {cls}: {x}')


sveta = User('Sveta')
del sveta

User.say_hello(123456)

class Singleton:
    obj = None

    def __new__(cls, *args, **kwargs):
        if cls.obj is None:
            cls.obj = object.__new__(cls, *args, **kwargs)
        return cls.obj


vasya = Singleton()
vasya.name = 'Vasya'
print(vasya.name)
petya = Singleton()
print(petya.name)
print(vasya is petya)

class Group:
    pass


group1 = Group()
group1.name = 'Admin'
print(group1.name)

group2 = Group()
print(group2.name)


# group2.name = 'Moder'
# print(group2.name)


def has_perm(self, perm):
    return True


Group.has_perm = has_perm
group2 = Group()
print(group2.has_perm('view all'))

class Multiplier:
    def __call__(self, x, y, z):
        return print(x * y * z)


mult = Multiplier()
mult(1, 2, 3)

class Collection:
    def __init__(self, lst):
        self.lst = lst
        self.lst2 = [1, 2, 3, 4, 5, 6, 7]

    def __len__(self):
        return len(self.lst) - 2


collection = Collection([1, 2, 3, 4])
print(len(collection))


