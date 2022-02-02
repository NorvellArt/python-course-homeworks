import geometry


class Pair:
    def __init__(self, a: int, b: int):
        self.a = a
        self.b = b

    def sum(self):
        return self.a + self.b

    def mul(self):
        return self.a * self.b


class RightTriangle(Pair):
    def __init__(self, a: int, b: int):
        super().__init__(a, b)

    def hypo(self):
        return round(geometry.sqrt(self.a ** 2 + self.b ** 2), 2)

    def print_hypo(self):
        hypo = self.hypo()
        print(f'Гипотенуза АВС: {hypo}')

    def square(self):
        return (self.a * self.b) * 0.5

    def print_square(self):
        square = self.square()
        return f'Площадь АВС: {square}'

    def print_info(self):
        hypo = self.hypo()
        return f'Прямоугольный треугольник АВС: ({self.a}, {self.b}, {hypo})'


triangle = RightTriangle(5, 8)
triangle.print_hypo()
print(triangle.print_info())
print(triangle.print_square())
print()
print(f'Сумма: {triangle.sum()}')
print(f'Произведение: {triangle.mul()}')
print()
triangle2 = RightTriangle(8, 10)
triangle2.print_hypo()
triangle2 = RightTriangle(10, 20)
triangle2.print_hypo()
print(f'Сумма: {triangle2.sum()}')
print(f'Произведение: {triangle2.mul()}')
print(triangle2.print_square())
