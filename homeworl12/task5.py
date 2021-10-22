def summator(*args):
    var = 0
    sum_list = []
    for i in list(args):
        sum_list.append(var + i)
        var += i
    for i in sum_list:
        print(i, sep=' ', end=' ')
    print()


summator(3, 9, 1)
summator(2, 5, 4, 2)
summator(3, 5, 10, 6, 3)
