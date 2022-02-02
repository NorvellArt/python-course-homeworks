from form import rectangle, circle


class Cylinder(rectangle.Rectangle, circle.Circle):
    def __init__(self, radius: int, height: int) -> None:
        self.radius = radius
        self.height = height

    def cylinder_volume(self):
        cylinder_volume = super().circle_square() * self.height
        return cylinder_volume

    def print_cylinder_volume(self):
        super().print_circle_square()
        print(f'Объем: {self.cylinder_volume():.2f}')

