print('Введите элементы списка:')
list1 = []
n = int(input('n = '))
for i in range(n):
    a = int(input('-> '))
    list1.append(a)
print('Введите число:')
ch = int(input('ch = '))

print('Число присутствует в элементах списка') if ch in list1 else print('Число не присутствует в элементах списка')
