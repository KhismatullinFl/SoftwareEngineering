def func(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
            if not content.strip():
                raise ValueError('Файл пустой')
            else:
                print(content)
        
    except ValueError as e:
        print(e)

if __name__ == '__main__':
    func('C:/Users/ivan7/Desktop/лабы/пи/10/f1.txt')
    func('C:/Users/ivan7/Desktop/лабы/пи/10/f2.txt')
    