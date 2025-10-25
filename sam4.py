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


