math = {'Matvei', 'Evgeniya', 'Mihail', 'Maxim', 'Natalia'}
physic = {'Maxim', 'Matvei', 'Alexandr'}
all_students = list(math | physic)
print('Все призеры:', all_students)
math.intersection_update(physic)
print('Призеры обеих олимпиад:', math)
print('Обновленный список призеров по математике:', math)
