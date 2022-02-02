import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def circle_length(self):
        circle_length = math.pi * (2 * self.radius)
        return circle_length

    def print_circle_length(self):
        print(f'Длина окружности: {self.circle_length():0.2f}')

    def circle_square(self):
        circle_square = math.pi * (self.radius ** 2)
        return circle_square

    def print_circle_square(self):
        print(f'Площадь окружности: {self.circle_square():0.2f}')
