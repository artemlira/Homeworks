line = input('Введите строку: ')
if 'x' not in line:
    print('Символа "x" нет в этой строке')
if 'w' not in line:
    print('Символа "w" нет в этой строке')
for i in line:
    if i in 'xw':
        print(i, 'встречается раньше')
        break
