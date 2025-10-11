def func(lst):
    d = {}
    for i in set(lst):
        d[i] = 0
    for i in lst:
        d[i] += 1

    result = set()
    for k, v in d.items():
        result.add(k)
        for r in range(2, v + 1):
            result.add(str(k) * r)
    return result

list_1 = [1, 1, 3, 3, 1]
list_2 = [5, 5, 5, 5, 5, 5, 5]
list_3 = [2, 2, 1, 2, 2, 5, 6, 7, 1, 3, 2, 2]

print(func(list_1))
print(func(list_2))
print(func(list_3))
