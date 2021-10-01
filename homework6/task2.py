import random

list1 = []
for i in range(20):
    list1.append(random.randint(0, 100))
print(list1)
print('Сумма: ', sum(list1))
