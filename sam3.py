import datetime
import time

def func(s):
    for i in range(s):
        now = datetime.datetime.now()
        print(now.strftime("%H:%M:%S"))
        time.sleep(1)

if __name__ == '__main__':
    func(5)
