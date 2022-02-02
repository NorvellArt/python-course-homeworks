import geometry


class Sphere:
    def __init__(self, r, x=0, y=0, z=0):
        self.__r = r
        self.__x = x
        self.__y = y
        self.__z = z

    def get_radius(self):
        return self.__r

    def get_volume(self):
        return (4 / 3) * geometry.pi * (self.__r ** 3)

    def get_square(self):
        return 4 * geometry.pi * self.__r ** 2

    def get_center(self):
        return self.__x, self.__y, self.__z

    def check_val(z):
        if isinstance(z, int) or isinstance(z, float):
            return True
        return False

    def is_point_inside(self, x, y, z):
        if Sphere.check_val(x) and Sphere.check_val(y) and Sphere.check_val(z):
            if self.__r >= geometry.fabs(x) and self.__r >= geometry.fabs(y) and self.__r >= geometry.fabs(z):
                return True
            return False
        else:
            print('Вводимые значения должны быть цифрами')

    def set_radius(self, r):
        if Sphere.check_val(r):
            self.__r = r
        else:
            print('Значение радиуса должно быть цифрой')

    def set_center(self, x, y, z):
        if Sphere.check_val(x) and Sphere.check_val(y) and Sphere.check_val(z):
            self.__x = x
            self.__y = y
            self.__z = z
        else:
            print('Вводимые значения должны быть цифрами')


sphere1 = Sphere(0.6)
print('get_radius:', sphere1.get_radius())
print('get_volume:', sphere1.get_volume())
print('get_square:', sphere1.get_square())
print('get_center:', sphere1.get_center())
print('get_square:', sphere1.get_square())
print('is_point_inside(0, -1.5, 0):', sphere1.is_point_inside(0, -1.5, 0))
sphere1.set_radius(1.6)
print('set_radius(1.6):', sphere1.get_radius())
print('is_point_inside(0, -1.5, 0):', sphere1.is_point_inside(0, -1.5, 0))
