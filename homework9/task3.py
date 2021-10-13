num = input('Введите по порядку, без пробелов, элементы кортежа: ')
tpl_num = tuple(num)
lst = []
print(tpl_num)
for i in tpl_num:
    if i not in lst:
        lst.append(i)
for i in lst:
    print('Количество', i, '=', tpl_num.count(i))

