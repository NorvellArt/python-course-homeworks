vowels = set('аоуэыяеёюи')
user_input = input('Введите строку: ')
count = 0
for i in user_input.lower():
    if i in vowels:
        count += 1
print('Количество гласных равно:', count)
