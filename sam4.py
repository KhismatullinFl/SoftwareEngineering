def language_detector(func):
    def wrapper():
        text = func()
        rus_alp = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
        eng_alp = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        
        rus_count = sum(1 for i in text if i in rus_alp)
        eng_count = sum(1 for i in text if i in eng_alp)
        
        if rus_count > eng_count and rus_count > 0:
            print('Русский')
        elif eng_count > rus_count and eng_count > 0:
            print('Английский')
        return func()
    return wrapper

@language_detector
def rus():
    text = 'Привет мир!'
    return text

@language_detector
def eng():
    text = 'Hello world!'
    return text

if __name__ == '__main__':
    print(rus())
    print(eng())
