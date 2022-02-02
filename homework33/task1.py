from abc import ABC, abstractmethod
import geometry


class Shape(ABC):
    @abstractmethod
    def perimetr(self):
        pass

    @abstractmethod
    def square(self):
        pass

    @abstractmethod
    def draw_figure(self):
        pass

    @abstractmethod
    def print_info(self):
        pass


class Rectangle(Shape):
    def __init__(self, length: int = 0, width: int = 0, color: str = 'green'):
        self.length = length
        self.width = width
        self.color = color

    def perimetr(self):
        print(f'Периметр: {2 * (self.length + self.width)}')

    def square(self):
        print(f'Площадь: {self.length * self.width}')

    def draw_figure(self):
        for i in range(self.length):
            for j in range(self.width):
                print('*', end='')
            print()

    def print_info(self):
        print('==Прямоугольник==')
        print(f'Длина: {self.length}')
        print(f'Ширина: {self.width}')
        print(f'Цвет: {self.color}')


class Square(Shape):
    def __init__(self, side: int = 0, color: str = 'red'):
        self.side = side
        self.color = color

    def perimetr(self):
        print(f'Периметр: {4 * self.side}')

    def square(self):
        print(f'Площадь: {self.side ** 2}')

    def draw_figure(self):
        for i in range(self.side):
            for j in range(self.side):
                print('*', end='')
            print()

    def print_info(self):
        print('==Квадрат==')
        print(f'Сторона: {self.side}')
        print(f'Цвет: {self.color}')


class Triangle(Shape):
    def __init__(self, side_1: int = 0, side_2: int = 0, side_3: int = 0, color: str = 'yellow'):
        self.side_1 = side_1
        self.side_2 = side_2
        self.side_3 = side_3
        self.color = color

    def perimetr(self):
        print(f'Периметр: {self.side_1 + self.side_2 + self.side_3}')

    def square(self):
        p = (self.side_1 + self.side_2 + self.side_3) / 2
        print(f'Площадь: {geometry.sqrt(p * (p - self.side_1) * (p - self.side_2) * (p - self.side_3))}')

    def draw_figure(self):
        for i in range(self.side_2):
            print(' ' * (self.side_2 - i) + '*' * (i + 1) + '*' * i)

    def print_info(self):
        print('==Треугольник==')
        print(f'Сторона 1: {self.side_1}')
        print(f'Сторона 2: {self.side_2}')
        print(f'Сторона 3: {self.side_3}')
        print(f'Цвет: {self.color}')


r1 = Rectangle(3, 7)
r1.print_info()
r1.square()
r1.perimetr()
r1.draw_figure()
print()
s1 = Square(3)
s1.print_info()
s1.square()
s1.perimetr()
s1.draw_figure()
print()
t1 = Triangle(11, 6, 6)
t1.print_info()
t1.square()
t1.perimetr()
t1.draw_figure()
