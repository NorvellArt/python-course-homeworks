import math


def distance(x1, x2, y1, y2):
    res = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return res


x1 = float(input('Введите х1: '))
y1 = float(input('Введите y1: '))
x2 = float(input('Введите х2: '))
y2 = float(input('Введите y2: '))
dist = distance(x1, x2, y1, y2)
print(round(dist, 2))
