import math


def quadratic_equation(a=2, b=3, c=-5):
    discriminant = (b ** 2) - (4 * a * c)
    roots = []
    if discriminant > 0:
        m = (math.sqrt(discriminant) - b) / (2 * a)
        n = (-math.sqrt(discriminant) - b) / (2 * a)
        roots.append(n)
        roots.append(m)
        return roots
    elif discriminant == 0:
        n = (-b) / (2 * a)
        roots.append(n)
        return roots
    else:
        return 'Дискриминант меньше нуля, уравнение не имеет действительных решений.'


print(quadratic_equation())
print(quadratic_equation(9, 6, 1))
print(quadratic_equation(2, -3, 4))