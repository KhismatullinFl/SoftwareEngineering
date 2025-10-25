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
