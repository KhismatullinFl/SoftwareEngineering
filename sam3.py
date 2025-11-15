def func():
    try:
        number = int(input())
        print(2 + number)
    except ValueError as vr:
        print(vr)

func()
