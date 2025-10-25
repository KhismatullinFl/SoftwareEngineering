with open('C:/Users/ivan7/Desktop/лабы/пи/7/lab1.txt', 'a') as f:
    f.write('\n Im additional line')
with open('C:/Users/ivan7/Desktop/лабы/пи/7/lab1.txt', 'r') as f:
    result = f.readlines()
    print(result)