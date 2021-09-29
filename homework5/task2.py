print('Введите элементы списка:')
n = int(input('n = '))
m = []
x = 0
for i in range(n):
    j = int(input('-> '))
    m.append(j)
for i in m:
    if x == 0:
        x = i
    else:
        if i > x:
            print(i, end=' ')
    x = i
