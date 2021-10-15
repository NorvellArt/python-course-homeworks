a = input('Введите первую строку: ')
b = input('Введите вторую строку: ')
print('Искомыми буквами являются:')
for i in set(a) - set(b):
    print(i, end=' ')
