from form import circle, rectangle, cylinder

circles = [circle.Circle(4), circle.Circle(2), circle.Circle(6), circle.Circle(8), circle.Circle(1)]
for circle in circles:
    circle.print_circle_length()
for circle in circles:
    circle.print_circle_square()
rects = [rectangle.Rectangle(3, 7), rectangle.Rectangle(2, 7), rectangle.Rectangle(19, 12)]
for rect in rects:
    rect.print_rectangle_perimeter()
cylinders = [cylinder.Cylinder(4, 7), cylinder.Cylinder(2, 5), cylinder.Cylinder(9, 3), cylinder.Cylinder(5, 5)]
for cylinder in cylinders:
    cylinder.print_cylinder_volume()
circle_max_s = max(circles, key=lambda c: c.circle_square())
rect_min_p = min(rects, key=lambda r: r.rectangle_perimeter())
cylinders_v = list(map(lambda c: c.cylinder_volume(), cylinders))
cylinders_v_avg = sum(cylinders_v) / len(cylinders_v)
print('*' * 50)
print(f'Окружность с наибольшей площадью: {circle_max_s.circle_square():.2f}')
print(f'Прямоугольник с наименьшим периметром: {rect_min_p.rectangle_perimeter():.2f}')
print(f'Средний объем всех цилиндров: {cylinders_v_avg:.2f}')
