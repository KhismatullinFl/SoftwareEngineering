def fib(n):
    a, b = 1, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

n = 200
last = None
for i, val in enumerate(fib(n), start=1):
    last = val
print(last)
