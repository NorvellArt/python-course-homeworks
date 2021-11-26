from funcs import opener, closer

opener()
pos1 = int(input('pos1 = '))
pos2 = int(input('pos2 = '))
f = open('text.txt', 'r')
lst = f.readlines()
lst[pos1], lst[pos2] = lst[pos2], lst[pos1]
f.close()
closer(lst)
