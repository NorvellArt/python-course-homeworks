students = [
    {'name': 'Jenifer', 'final': 95},
    {'name': 'David', 'final': 92},
    {'name': 'Nikolas', 'final': 98},
]

res = sorted(students, key=lambda item: item['name'])
print(res)
res = sorted(students, key=lambda item: item['final'], reverse=True)
print(res)
