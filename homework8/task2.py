def isPrime(n):
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n and n % d != 0:
        d += 2
    return d * d > n


list1 = [6, 3, 8, 5, 7, 9, 3, 6, 5, 13, 1]
prime = []
print(list1)
for i in list1:
    if isPrime(i):
        prime.append(i)
for i in prime:
    if i in list1:
        list1.remove(i)
print('Min: ', min(prime))
print('Max: ', max(list1))
