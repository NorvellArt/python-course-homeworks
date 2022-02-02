class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def rectangle_perimeter(self):
        rectangle_perimeter = 2 * (self.a + self.b)
        return rectangle_perimeter

    def print_rectangle_perimeter(self):
        print(f'Периметр прямоугольника: {self.rectangle_perimeter()}')

    def rectangle_square(self):
        rectangle_square = self.a * self.b
        return rectangle_square

    def print_rectangle_square(self):
        print(f'Площадь прямоугольника: {self.rectangle_square()}')
