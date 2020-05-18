number = input('Введите номер билета ')
l = len(number) // 2
first, last = list(map(int, number[:l])), list(map(int, number[l:]))
if sum(first) == sum(last):
    print('Билет счастливый')
else:
    print('Былет не счастливый')
