import random

list1 = []
for i in range(10):
    list1.append(random.randint(0, 100))
print(list1)
print(sorted(list1, reverse=True))


