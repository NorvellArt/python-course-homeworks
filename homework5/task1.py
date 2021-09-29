print('Введите элементы списка:')
n = int(input('n = '))
m = []
for i in range(n):
    j = int(input('-> '))
    m.append(j)
for i in range(0, len(m), 2):
    print(m[i], end=' ')
