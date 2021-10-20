dict1 = {
    'emp1': {
        'name': 'Jhon',
        'salary': 7500
    },
    'emp2': {
        'name': 'Emma',
        'salary': 8000
    },
    'emp3': {
        'name': 'Brad',
        'salary': 6500
    },
}

print(dict1['emp3'])
print(dict1['emp3']['salary'])

dict1['emp3']['salary'] = 8000

for i in dict1:
    print(i)
    print('name:', dict1[i]['name'])
    print('salary:', dict1[i]['salary'])
