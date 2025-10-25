with open('C:/Users/ivan7/Desktop/лабы/пи/7/input2.txt', 'a+', encoding='utf-8') as f:
    while (True):
        s = input('Введите ваш расход: ')
        f.write(f'{s}\n')
        f.seek(0)     
        print(f.read())