# Тема 7. РАБОТА С ФАЙЛАМИ (ВВОД, ВЫВОД).
Отчет по Теме #7 выполнил(а):
- Хисматуллин Андрей Дмитриевич
- ПИЭ-23-1

| Задание | Лаб_раб | Сам_раб |
| ------ | ------ | ------ |
| Задание 1 | + | + |
| Задание 2 | + | + |
| Задание 3 | + | + |
| Задание 4 | + | + |
| Задание 5 | + | + |
| Задание 6 | + |
| Задание 7 | + |
| Задание 8 | + |
| Задание 9 | + |
| Задание 10 | + |


знак '+' - задание выполнено; знак '-' - задание не выполнено;

Работу проверили:
- к.э.н., доцент Панов М.А.

## Лабораторная работа №1
### Составьте текстовый файл и положите его в одну директорию с программой на Python. Текстовый файл должен состоять минимум из двух строк.


### Результат.
![Меню](https://github.com/KhismatullinFl/SoftwareEngineering/blob/tema_7/images/l1.png)

## Выводы
Текст

## Лабораторная работа №2
### Напишите программу, которая выведет только первую строку из вашего файла, при этом используйте конструкцию open()/close().

```python
f = open('C:/Users/ivan7/Desktop/лабы/пи/7/lab1.txt', 'r')
print(f.readline())
f.close()
```
### Результат.
![Меню](https://github.com/KhismatullinFl/SoftwareEngineering/blob/tema_7/images/l2.png)

## Выводы
Код открывает текстовый файл на компьютере и выводит первую строку из этого файла на экран.

## Лабораторная работа №3
### Напишите программу, которая выведет все строки из вашего файла в массиве, при этом используйте конструкцию open()/close().

```python
f = open('C:/Users/ivan7/Desktop/лабы/пи/7/lab1.txt', 'r')
print(f.readlines())
f.close()
```
### Результат.
![Меню](https://github.com/KhismatullinFl/SoftwareEngineering/blob/tema_7/images/l3.png)

## Выводы
Код открывает текстовый файл, считывает все его строки и выводит их на экран в виде списка.

## Лабораторная работа №4
### Напишите программу, которая выведет все строки из вашего файла в массиве, при этом используйте конструкцию with open()

```python
with open('C:/Users/ivan7/Desktop/лабы/пи/7/lab1.txt') as f:
    print(f.readlines())
```
### Результат.
![Меню](https://github.com/KhismatullinFl/SoftwareEngineering/blob/tema_7/images/l4.png)

## Выводы
Код открывает текстовый файл, считывает все его строки и выводит их на экран в виде списка.

## Лабораторная работа №5
### Напишите программу, которая выведет каждую строку из вашего файла отдельно, при этом используйте конструкцию with open().

```python
with open("C:/Users/ivan7/Desktop/лабы/пи/7/lab1.txt") as f:
    for Line in f:
        print(Line)
```
### Результат.
![Меню](https://github.com/KhismatullinFl/SoftwareEngineering/blob/tema_7/images/l5.png)

## Выводы
Код открывает текстовый файл и выводит каждую его строку по одной на экран.

## Лабораторная работа №6
### Напишите программу, которая будет добавлять новую строку в ваш файл, а потом выведет полученный файл в консоль. Вывод можно осуществлять любым способом. Обязательно проверьте сам файл, чтобы изменения в нем тоже отображались.

```python
with open('C:/Users/ivan7/Desktop/лабы/пи/7/lab1.txt', 'a') as f:
    f.write('\n Im additional line')
with open('C:/Users/ivan7/Desktop/лабы/пи/7/lab1.txt', 'r') as f:
    result = f.readlines()
    print(result)
```
### Результат.
![Меню](https://github.com/KhismatullinFl/SoftwareEngineering/blob/tema_7/images/l1.png)

## Выводы
Код добавляет новую строку в текстовый файл, а затем выводит все его содержимое на экран.

## Лабораторная работа №7
### Напишите программу, которая перепишет всю информацию, которая была у вас в файле до этого, например напишет любые данные из произвольно вами составленного списка. Также не забудьте проверить что измененная вами информация сохранилась в файле.

```python
Lines = ['one', 'two', 'three']
with open('C:/Users/ivan7/Desktop/лабы/пи/7/lab1.txt', 'w') as f:
    for Line in Lines:
        f.write('\nCycle run line')
        print("Done!")
```
### Результат.
![Меню](https://github.com/KhismatullinFl/SoftwareEngineering/blob/tema_7/images/l2.png)

## Выводы
Код перезаписывает текстовый файл, записывая фразу 3 раза.

## Лабораторная работа №8
### Выберите любую папку на своем компьютере, имеющую вложенные директории. Выведите на печать в терминал ее содержимое, как и всех подкаталогов при помощи функции print_docs(directory).

```python
import os

def print_docs(directory):
    all_files = os.walk(directory)
    for catalog in all_files:
        print(f'Папка {catalog[0]} содержит:')
        print (f'Директории: {", ".join([folder for folder in catalog[1]])}')
        print (f'Файлы: {", ".join([file for file in catalog [2]])}')
        print('-'*40)
print_docs('C:/Users/ivan7/Desktop/лабы/пи')
```
### Результат.
![Меню](https://github.com/KhismatullinFl/SoftwareEngineering/blob/tema_7/images/l3.png)

## Выводы
Код обходит указанную папку и все ее подпапки, выводя для каждой папки список содержащихся в ней директорий и файлов.

## Лабораторная работа №9
### Документ «input.txt» содержит следующий текст: Приветствие Спасибо Извините Пожалуйста До свидания Ты готов? Как дела? С днем рождения! Удача! Я тебя люблю. Требуется реализовать функцию, которая выводит слово, имеющее максимальную длину (или список слов, если таковых несколько). Проверьте работоспособность программы на своем наборе данных

```python
def longest_words(file):
    with open(file, encoding='utf-8') as f:
        words = f.read().split()
        max_length = len(max(words, key=len))
        for word in words:
            if len(word) == max_length:
                sought_words = word
            if len(sought_words) == 1:
                return sought_words[8]
            return sought_words

print(longest_words('C:/Users/ivan7/Desktop/лабы/пи/7/input.txt'))
```
### Результат.
![Меню](https://github.com/KhismatullinFl/SoftwareEngineering/blob/tema_7/images/l4.png)

## Выводы
Код находит самое длинное слово в файле и выводит.

## Лабораторная работа №10
### Требуется создать csv-файл «rows_300.csv» со следующими столбцами: • № - номер по порядку (от 1 до 300); • Секунда – текущая секунда на вашем ПК; • Микросекунда – текущая миллисекунда на часах. Для наглядности на каждой итерации цикла искусственно приостанавливайте скрипт на 0,01 секунды.

```python
import csv
import datetime
import time
with open('C:/Users/ivan7/Desktop/лабы/пи/7/rows_300.csv', 'w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow (['", "Секунда, Микросекунда'])
    for line in range(1, 301):
        writer.writerow([line, datetime.datetime.now().second,
        datetime.datetime.now().microsecond])
        time.sleep(0.01)
```
### Результат.
![Меню](https://github.com/KhismatullinFl/SoftwareEngineering/blob/tema_7/images/l5.png)

## Выводы
Код создает CSV файл, в котором каждая строка содержит номер строки, текущую секунду и микросекунду, с задержкой в 0.01 секунды между каждой записью.

## Самостоятельная работа №1
### Найдите в интернете любую статью (объем статьи не менее 200 слов), скопируйте ее содержимое в файл и напишите программу, которая считает количество слов в текстовом файле и определит самое часто встречающееся слово. Результатом выполнения задачи будет: скриншот файла со статьей, листинг кода, и вывод в консоль, в котором будет указана вся необходимая информация

```python
with open('C:/Users/ivan7/Desktop/лабы/пи/7/input1.txt', encoding='utf-8') as f:
    text = f.read()
    words = {}
    count = 0
    word = ''
    for i in text:
        if i.isalnum():
            word += i.lower()
        else:
            if word:
                words[word] = words.get(word, 0) + 1
                count += 1
                word = ''
    if word:
        words[word] = words.get(word, 0) + 1
        count += 1

    k, v = max(words.items(), key=lambda kv: kv[1])
    print('Всего слов:', count)
    print(f'Самое частое слово {k} встречается {v}')

```
### Результат.
![Меню](https://github.com/KhismatullinFl/SoftwareEngineering/blob/tema_7/images/s1.png)

## Выводы
Код читает текст из файла, подсчитывает общее количество слов и находит самое частое, выводя эти результаты на экран.

## Самостоятельная работа №2
### У вас появилась потребность в ведении книги расходов, посмотрев все существующие варианты вы пришли к выводу что вас ничего не устраивает и нужно все делать самому. Напишите программу для учета расходов. Программа должна позволять вводить информацию о расходах, сохранять ее в файл и выводить существующие данные в консоль. Ввод информации происходит через консоль. Результатом выполнения задачи будет: скриншот файла с учетом расходов, листинг кода, и вывод в консоль, с демонстрацией работоспособности программы

```python
with open('C:/Users/ivan7/Desktop/лабы/пи/7/input2.txt', 'a+', encoding='utf-8') as f:
    while (True):
        s = input('Введите ваш расход: ')
        f.write(f'{s}\n')
        f.seek(0)     
        print(f.read())
```
### Результат.
![Меню](https://github.com/KhismatullinFl/SoftwareEngineering/blob/tema_7/images/s2.png)

## Выводы
Код записывает вводимые пользователем расходы в файл и выводит содержимое всего файла на экран.

## Самостоятельная работа №3
### Имеется файл input.txt с текстом на латинице. Напишите программу, которая выводит следующую статистику по тексту: количество букв латинского алфавита; число слов; число строк. • Текст в файле: Beautiful is better than ugly. Explicit is better than implicit. Simple is better than complex. Complex is better than complicated. • Ожидаемый результат: Input file contains: 108 letters 20 words 4 lines

```python
with open('C:/Users/ivan7/Desktop/лабы/пи/7/input3.txt', 'r', encoding='utf-8') as f:
    text = f.read()

    lines = text.splitlines()
    print("Input file contains:")
    print(f"{len(text.replace(' ','').replace('.',''))} letters")
    print(f"{len(text.split())} words")
    print(f"{len(lines)} lines")

```
### Результат.
![Меню](https://github.com/KhismatullinFl/SoftwareEngineering/blob/tema_7/images/s3.png)

## Выводы
Код открывает текстовый файл, подсчитывает в нем количество букв, слов и строк, а затем выводит эти данные на экран.

## Самостоятельная работа №4
### Напишите программу, которая получает на вход предложение, выводит его в терминал, заменяя все запрещенные слова звездочками * (количество звездочек равно количеству букв в слове). Запрещенные слова, разделенные символом пробела, хранятся в текстовом файле input.txt. Все слова в этом файле записаны в нижнем регистре. Программа должна заменить запрещенные слова, где бы они ни встречались, даже в середине другого слова. Замена производится независимо от регистра: если Михаил А. Панов файл input.txt содержит запрещенное слово exam, то слова exam, Exam, ExaM, EXAM и exAm должны быть заменены на ****. • Запрещенные слова: hello email python the exam wor is • Предложение для проверки: Hello, world! Python IS the programming language of thE future. My EMAIL is.... PYTHON is awesome!!!! • Ожидаемый результат: *****, ***ld! ****** ** *** programming language of *** future. My ***** **.... ****** ** awesome!!!!

```python
with open('C:/Users/ivan7/Desktop/лабы/пи/7/input4.txt', 'r', encoding='utf-8') as f:
    l = f.read().split()  
    s = input()

    n = len(s)
    low = s.lower()
    mask = [False] * n

    for w in l:
        w = w.lower()
        m = len(w)
        if m == 0:
            continue
        for i in range(n - m + 1):
            if low[i:i+m] == w:
                for j in range(i, i+m):
                    mask[j] = True

    out = []
    for i, ch in enumerate(s):
        if mask[i]:
            out.append('*')
        else:
            out.append(ch)

    print(''.join(out))
```
### Результат.
![Меню](https://github.com/KhismatullinFl/SoftwareEngineering/blob/tema_7/images/s4.png)

## Выводы
Код читает слова из файла, а затем заменяет все их вхождения в строке, введенной пользователем, на звездочки.

## Самостоятельная работа №5
### Самостоятельно придумайте и решите задачу, которая будет взаимодействовать с текстовым файлом. Напишите программу, которая получает на вход текст их файла, выводит его в терминал в обратном порядке.

```python
with open('C:/Users/ivan7/Desktop/лабы/пи/7/input1.txt', 'r', encoding='utf-8') as f:
    text = f.read()
    print(text[::-1])
```
### Результат.
![Меню](https://github.com/KhismatullinFl/SoftwareEngineering/blob/tema_7/images/s5.png)

## Выводы
Код открывает текстовый файл и выводит его содержимое на экран в обратном порядке.

## Общие выводы по теме
В ходе лабораторной работы по теме 'Работа с файлами (ввод, вывод)' я освоил основные принципы взаимодействия с файловой системой Python, научившись открывать файлы в различных режимах (чтение, запись, добавление), эффективно считывать данные построчно или целиком, а также записывать информацию, что позволило мне уверенно применять эти знания для обработки и управления текстовыми данными в дальнейшем.