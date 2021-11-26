from funcs import opener, closer

opener()
f = open('text.txt', 'r')
lst = f.readlines()
lst.reverse()
f.close()
closer(lst)
