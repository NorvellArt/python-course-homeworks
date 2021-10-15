a = set(input('Введите первую строку: '))
b = set(input('Введите вторую строку: '))
print('Искомыми буквами являются:')
a.symmetric_difference_update(b)
for i in a:
    print(i, end=' ')
