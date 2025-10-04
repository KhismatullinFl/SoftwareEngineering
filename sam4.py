def mean(*args):
    return sum(args) / len(args)

if __name__ == '__main__':
    s = input('Введите числа через пробел: ').strip()
    nums = [float(x) for x in s.split()]
    print('Среднее арифметическое:', mean(*nums))
