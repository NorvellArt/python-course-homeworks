string = '''Ежевику для ежат
            Принесли два ежа.
            Ежевику еле-еле
            Ежата возле ели съели.'''
count = 0
s = string.split('\n')
s = [x for i in s for x in i.strip().split()]
for i in s:
    if i[0].lower() == 'е':
        count += 1

print('Количество слов:', count)


