values = [0, 2, 4, 6, 8, 10]
string = ' world'
memory = string
string = 'hello'
counter = 0

while 'world' not in string:
    if counter in values:
        print(string + memory)
        print(string)
    if counter > 7:
        string = string + ' world'
        memory = string
        print(memory)
        memory = 'world'
        string = memory
    counter += 1