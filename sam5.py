def func(t):
    return tuple(x for x in t if x % 2 == 0)

print(func((1, 2, 3, 4, 5)))
print(func((0, -2, 7, 8)))
print(func((1, 3, 5)))
