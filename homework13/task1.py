import math


def figure_func(figure, **kwargs):
    if figure == 'rhombus':
        s = (kwargs['d1'] * kwargs['d2']) / 2
    elif figure == 'square':
        s = kwargs['a'] ** 2
    elif figure == 'trapezoid':
        s = ((kwargs['a'] + kwargs['b']) * kwargs['h']) / 2
    elif figure == 'circle':
        s = (math.pi * kwargs['r'] ** 2)
    else:
        return 'invalid data'
    return s


print(figure_func('rhombus', d1=10, d2=8))
print(figure_func('square', a=5))
print(figure_func('trapezoid', a=12, b=3, h=6))
print(figure_func('circle', r=18))
print(figure_func('unknown', a=1, b=2, c=3))
