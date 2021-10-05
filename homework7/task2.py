import math


def triangle(a, b, c):
    res = ((a * b) / 2) * math.sin(math.radians(c))
    return res


a = int(input('Сторона 1: '))
b = int(input('Сторона 2: '))
c = int(input('Угол: '))
d = triangle(a, b, c)
print(round(d, 2))
