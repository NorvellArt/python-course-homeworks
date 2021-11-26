from funcs import opener, closer

opener()
pos = int(input('pos = '))
f = open('text.txt', 'r')
lst = f.readlines()
lst.pop(pos)
f.close()
closer(lst)
