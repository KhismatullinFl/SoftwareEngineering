import random

def func():
    value = random.randint(1, 6)
    print(f"Значение кубика: {value}")
    if value in (5, 6):
        print('Вы победили')
    elif value in (1, 2):
        print('Вы проиграли')
    else:  
        func()

if __name__ == '__main__':
    func()
