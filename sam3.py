with open('C:/Users/ivan7/Desktop/лабы/пи/7/input3.txt', 'r', encoding='utf-8') as f:
    text = f.read()

    lines = text.splitlines()
    print("Input file contains:")
    print(f"{len(text.replace(' ','').replace('.',''))} letters")
    print(f"{len(text.split())} words")
    print(f"{len(lines)} lines")
