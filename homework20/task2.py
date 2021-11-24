num_list = [-2, 3, 8, -11, -4, 6]


def count_below_zero_nums(lst):
    if not lst:
        return False
    else:
        count = count_below_zero_nums(lst[1:])
        if lst[0] < 0:
            count += 1

        return count


print(num_list)
print('n =', count_below_zero_nums(num_list))
