s = '012345363738494'
print('s =', s)


def delete_number(string, number):
    string = list(string)
    for i in string:
        if i == str(number):
            string.remove(i)
    return ''.join(string)


s2 = delete_number(s, 3)
print('s2 =', s2)
