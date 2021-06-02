import time
import sys
from multiprocessing import Process
time1 = time.time()
def one():
    while True:
        print('woani')
        time2 = time.time()
        s = time2 - time1
        print(s)
        if s > 5:
            sys.exit(1)
def two():
    while True:
        print('123')

if __name__ == '__main__':
    p1 = Process(target=one)
    p2 = Process(target=two)
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print('13211111111111111111111111111111111111111111111111111111111')
