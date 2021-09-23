print('-' * 50)
print('Первое решение:')
a = 123
b = 321
print('a =', a, 'b =', b)
a, b = b, a
print('a =', a, 'b =', b)
print('-' * 50)
print('Второе решение:')
a = 123
b = 321
print('a =', a, 'b =', b)
a = a + b
b = a - b
a = a - b
print('a =', a, 'b =', b)
print('-' * 50)
print('Третье решение:')
a = 123
b = 321
print('a =', a, 'b =', b)
a = a ^ b
b = a ^ b
a = a ^ b
print('a =', a, 'b =', b)
print('-' * 50)

