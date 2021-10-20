a, b, c = {1: 10, 2: 20}, {3: 30, 4: 40}, {5: 50, 6: 60}
z = a.copy()
z.update(b)
z.update(c)
print(z)
