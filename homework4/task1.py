num = input('Введите число: ')
reverse = num[::-1]
print('Число', num, '- палиндром') \
    if num == reverse \
    else print('Число', num, '- не палиндром')
