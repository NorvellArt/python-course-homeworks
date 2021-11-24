import random


def binary_search(s, item):
    first = 0
    last = len(s) - 1
    found = False

    while first <= last and not found:
        middle_point = (first + last) // 2
        if s[middle_point] == item:
            found = True
        else:
            if item < s[middle_point]:
                last = middle_point - 1
            else:
                first = middle_point + 1

    return found


random_list = [random.randint(1, 100) for i in range(10)]
print(random_list)
random_list.sort()
user_input = int(input('Введите число: '))
if binary_search(random_list, user_input):
    print(f'Число {user_input} присутствует в списке')
else:
    print(f'Число {user_input} не найдено в списке')
