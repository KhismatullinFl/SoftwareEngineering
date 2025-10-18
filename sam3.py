def func(s):
    dict = {i: 0 for i in range(10)}
    for i in s:
        dict[int(i)]+=1
    items = sorted(((d, c) for d, c in dict.items()),
                   key=lambda x: (-x[1], x[0]))
    
    top = {d: c for d, c in items[:3]}
    return top
print(func('1231546616549842348949845456154878945665487463845613'))