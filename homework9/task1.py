def func13(*args):
    lst = []
    for i in args:
        if i % 13 == 0 and i > 0:
            lst.append(i)
    if len(lst) != 0:
        return max(lst)
    else:
        return 'no such numbers'


print(func13(2, 7, 0, 3, 1, 5, -13))
print(func13(2, 7, 0, 3, 1, 5, -13, 13))
print(func13(26))
print(func13(99, 99, 100, 34, -39))
print(func13(99, 39, 99, 100, 34))
