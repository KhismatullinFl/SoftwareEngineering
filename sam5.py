class Ex(Exception):
    pass

def func(name):
    rus_alp = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    try:
        if any(i not in rus_alp for i in name):
            raise Ex(f'Имя {name} содержит некорректные символы')
        print(name)
    except Ex as e:
        print('Ошибка', e)

name1 = 'ivan'
name2 = 'леха2005'
name3 = 'андрей'
func(name1)
func(name2)
func(name3)


