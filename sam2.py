def fib(n):
    a, b = 1, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

n = 200
last = None
with open('C:/Users/ivan7/Desktop/лабы/пи/11/fib.txt', 'w', encoding='utf-8') as f:
    for i, v in enumerate(fib(n), start=1):
        f.write(str(v) + "\n")
        last = v
print(last)
