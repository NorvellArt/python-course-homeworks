# 1 задание
name = input('What is you name? ')
age = int(input('How old are you? '))
city = input('Where are you live? ')
print("This is {0}\nIt is {1}\nHe lives in {2}".format(name, age, city))
print('-' * 80)
# 2 задание
print("Решите пример: 4 * 100 - 54")
answer = int(input('Ваш ответ: '))
print("Правильный ответ: 346")
print("Ваш ответ: {0}".format(answer))
print('-' * 80)
# 3 задание
num = int(input("Введите число: "))
print('Четное' if (num % 2 == 0) else 'Нечетное')