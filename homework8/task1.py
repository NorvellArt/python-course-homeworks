import geometry


def square(a, b):
    return a * b


def triangle(a, h):
    return 0.5 * a * h


def circle(r):
    return geometry.pi * (r ** 2)


user_chose = int(input('1 - прямоугольник, 2 - треугольник, 3 - круг: '))
if user_chose == 1:
    a = int(input('Сторона 1: '))
    b = int(input('Сторона 2: '))
    c = square(a, b)
    print('Площадь:', c)
elif user_chose == 2:
    a = int(input('Основание: '))
    b = int(input('Высота: '))
    c = triangle(a, b)
    print('Площадь:', c)
elif user_chose == 3:
    a = int(input('Радиус: '))
    c = circle(a)
    print('Площадь:', c)
else:
    print('Вы ввели неправильное число')
