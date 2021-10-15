def set_gen(lst):
    new_list = list(set(lst))
    new_set = set(lst)
    count = 1
    for i in new_list:
        while count < lst.count(i):
            count += 1
            new_set.add(str(i) * count)
        count = 1
    return new_set


print(set_gen([1, 1, 3, 3, 1]))
print(set_gen([5, 5, 5, 5, 5, 5, 5]))
print(set_gen([2, 2, 1, 2, 2, 5, 6, 7, 1, 3, 2, 2]))
