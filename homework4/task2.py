a = int(input('Начало диапазона: '))
b = int(input('Конец диапазона: '))
for i in range(a, b + 1):
    if i % 2 != 0:
        print(i, end=' ')
