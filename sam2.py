def func(t, a):
    if a in t:
        i = t.index(a)
        return t[:i] + t[i+1:]
    return t
    
print(func((1, 2, 3), 1))
print(func((1, 2, 3, 1, 2, 3, 4, 5, 2, 3, 4, 2, 4, 2), 3))
print(func((2, 4, 6, 6, 4, 2), 9))