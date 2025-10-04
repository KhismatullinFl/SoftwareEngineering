import math

def func(a, b, c):
    p = (a+b+c)/2
    s = p*(p-a)*(p-b)*(p-c)
    return math.sqrt(s)
