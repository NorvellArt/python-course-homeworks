count = int(input('Количество символов: '))
symbol = input('Тип символа: ')
print('0 - горизонтальная')
print('1 - вертикальная')
orient = int(input('Ориентация линии: '))
if orient == 0:
    while count > 0:
        print(symbol, end='')
        count -= 1
elif orient == 1:
    while count > 0:
        print(symbol)
        count -= 1
else:
    print('Введите 0 или 1')
