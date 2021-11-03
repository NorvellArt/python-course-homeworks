students = [
    {'name': 'Jenifer', 'final': 95},
    {'name': 'David', 'final': 92},
    {'name': 'Nikolas', 'final': 98},
]

minimum = sorted(students, key=lambda item: item['final'])[0]
print(minimum)
maximum = sorted(students, key=lambda item: item['final'], reverse=True)[0]
print(maximum)
