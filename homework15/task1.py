def func_compute(a):
    def inner_func(b):
        return a * b
    return inner_func


res = func_compute(2)
print(res(15))
print(res(20))
res = func_compute(3)
print(res(15))
print(res(20))
