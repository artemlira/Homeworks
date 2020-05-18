class Mammal:
    type_name = 'Млекопетающие'


# class Cat(Mammal):
#     paw = 4
#
#
# cat = Cat()
# print(cat.paw)
# print(cat.type_name)


class Horse(Mammal):
    is_horse = True

    def move(self):
        print('OK')


class Donkey(Mammal):
    is_donkey = True

    def move(self):
        print('KO')


class Mule(Horse, Donkey):
    is_mule = True
    is_horse = False


horse = Horse()
donkey = Donkey()
mule = Mule()
# print(horse.is_horse)
# print(donkey.is_donkey)
# print(mule.is_mule)
# print(mule.is_horse)
# print(mule.is_donkey)
# print(mule.type_name)
print(mule.move())
