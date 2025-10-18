def func(t, a):
    if a not in t:
        return ()
    first = t.index(a)
    if (a in t[first+1:]):
        second = t.index(a, first + 1)
        return t[first:second + 1]
    return t[first:]
print(func((1, 2, 3), 8))
print(func((1, 8, 3, 4, 8, 8, 9, 2), 8)) 
print(func((1, 2, 8, 5, 1, 2, 9), 8))
