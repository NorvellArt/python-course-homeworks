count = int(input("Введите количество чисел последовательности: "))
maxNum = 0
minNum = 0
avg = 0
seq = count
while count > 0:
    a = float(input('Введите число: '))
    if maxNum:
        if a > maxNum:
            maxNum = a
    else:
        maxNum = a
    if minNum:
        if a < minNum:
            minNum = a
    else:
        minNum = a
    avg += a
    count -= 1
print('Количество чисел:', seq)
print('Среднее арифметическое:', avg / seq)
print('Минимальное число:', minNum)
print('Максимальное число:', maxNum)


