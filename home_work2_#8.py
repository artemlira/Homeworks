import random

a = []
b = a[::-1]
for i in range(4):
    a.append(int(random.random() * 20))
print(a)
print('Число является палиндромом' if a[0:1] == b[0:1] else 'Число не является палиндромом')
