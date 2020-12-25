"""
   复制照片
"""
from multiprocessing import Process
import os
filename = './123.jpg'
c = open(filename,'rb')
n = os.path.getsize(filename)
"""
父进程中创建IO，子进程从父进程中获取IO对象，实际上他们操作的是同一个io，
属性互相影响
如果在各自进程中创建IO对象，那么这些IO对象互相没有影响
"""
def top():
    rw = open('top.jpg','wb')
    rw.write(c.read(n//2))
    rw.close()
def bot():
    rw = open('bot.jpg','wb')
    rw.write(c.read(n//2))
    rw.close()
p1 =Process(target=top)
p2 =Process(target=bot)
p1.start()
p2.start()
p1.join()
p2.join()
c.close()


