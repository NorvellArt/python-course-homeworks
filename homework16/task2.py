s = '0123456789'
print('s =', s)


def delete_by_index(string, index):
    string = list(string)
    string.pop(index)
    return ''.join(string)


s2 = delete_by_index(s, 4)
print('s2 =', s2)
