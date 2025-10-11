list1 = [2, 3, 4, 5, 3, 4, 5, 2, 2, 5, 3, 4, 3, 5, 4]
list2 = [4, 2, 3, 5, 3, 5, 4, 2, 2, 5, 4, 3, 5, 3, 4]
list3 = [5, 4, 3, 3, 4, 3, 3, 5, 5, 3, 3, 3, 3, 4, 4]

def func(l):
    result = []
    for i in l:
        if i == 2:
            continue
        elif i == 3:
            result.append(4)
        else:
            result.append(i)
    return result

print('Список 1:', func(list1))
print('Список 2:', func(list2))
print('Список 3:', func(list3))