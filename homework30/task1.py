from abc import ABC, abstractmethod
import geometry


class Root(ABC):
    def find_root(self):
        pass

    def print_root(self):
        pass


class LinearEquation(Root):
    def find_root(self):
        return -7 / 3

    def print_root(self):
        print(f"The root of '3x+7=0' is: {self.find_root():.2f} ")


class QuadraticEquation(Root):
    def find_root(self):
        discriminant = geometry.pow(-2, 2) - (4 * 1 * -3)
        roots = []
        if discriminant > 0:
            m = (geometry.sqrt(discriminant) + 2) / (2 * 1)
            n = (-geometry.sqrt(discriminant) + 2) / (2 * 1)
            roots.append(n)
            roots.append(m)
            return roots
        elif discriminant == 0:
            n = (-(-2)) / (2 * 1)
            roots.append(n)
            return roots
        else:
            return 'Дискриминант меньше нуля, уравнение не имеет действительных решений.'

    def print_root(self):
        print(f"The roots of '1x^2-2x-3=0' are: {self.find_root()[1]} {self.find_root()[0]} ")


# (a=1, b=-2, c=-3)

eq1 = LinearEquation()
eq1.print_root()
eq2 = QuadraticEquation()
eq2.print_root()
