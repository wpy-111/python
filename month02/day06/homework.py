"""
   使用Prcess创建两个子进程，同时复制一个文件，分别复制文件的前半部分和后半部分
"""
ADDR = '/home/tarena/wpy/DataStructure/day01/singlelink.py'
import os
import multiprocessing as mp
m = os.path.getsize(ADDR)
c = open(ADDR,'rb')
s = open('file01','wb')
b = open('file02','wb')
def fun01():
    s.write(c.read(int(m/2)))
    s.flush()
    s.close()
    return c.tell()

p = mp.Process(target=fun01)
p.start()
b.seek(fun01())
b.write(c.read(int(m / 2)))
b.flush()
b.close()
p.join()