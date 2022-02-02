class ValidNumber:
    def __set_name__(self, owner, number):
        self.__number = number

    def __get__(self, instance, owner):
        return instance.__dict__[self.__number]

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise ValueError(f'Должно быть целым числом')
        instance.__dict__[self.__number] = value


class Point3D:
    x = ValidNumber()
    y = ValidNumber()
    z = ValidNumber()

    def __init__(self, x, y, z):
        self._x = x
        self._y = y
        self._z = z


p = Point3D(1, 2, 3)
print(p.__dict__)

