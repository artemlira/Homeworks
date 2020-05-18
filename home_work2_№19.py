import random

a = []
for i in range(10):
    a.append(int(random.random() * 100))
print(a)
even = 1

for i in a:
    if i % 2 == 0:
        even *= i

print('Произведение четных элементов последовательности: ', even)
