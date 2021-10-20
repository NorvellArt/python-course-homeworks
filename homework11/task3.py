students_number = int(input('Количество студентов: '))
students_dict = {}
avg = 0
for i in range(students_number):
    name = input('{}-й студент: '.format(i+1))
    score = int(input('Балл: '))
    students_dict.update({name: score})
for i in list(students_dict.values()):
    avg += i
avg = avg / students_number
print('Средний балл:', avg, '. Студенты с баллом выше среднего:')
for key, value in students_dict.items():
    if value > avg:
        print(key)

