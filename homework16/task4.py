def ten_to_two(n):
    b = ''
    while n:
        b = str(n % 2) + b
        n = n // 2
    return b


def repeater(func, n=True):
    while n:
        n = int(input('-> '))
        print(func(n))


repeater(ten_to_two)
