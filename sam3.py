import math

def func(a, b, c):
    p = (a+b+c)/2
    s = p*(p-a)*(p-b)*(p-c)
    return math.sqrt(s)

one = [12, 25, 3, 48, 71]
two = [5, 18, 40, 62, 98]
three = [4, 21, 37, 56, 84]

print('Максимальная площадь:', func(max(one), max(two), max(three)))
print('Минимальная площадь:', func(min(one), min(two), min(three)))
