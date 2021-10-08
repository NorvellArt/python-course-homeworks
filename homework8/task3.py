def summa(n, even=True):
    s = 0
    while n > 0:
        a = n % 10
        if even and a % 2 == 0:
            s += a
        elif not even and a % 2 != 0:
            s += a
        n //= 10
    return s


print('Сумма четных цифр:')
print(summa(9874023))
print(summa(38271))
print(summa(123456789))
print('Сумма нечетных цифр:')
print(summa(9874023, even=False))
print(summa(38271, even=False))
print(summa(123456789, even=False))
