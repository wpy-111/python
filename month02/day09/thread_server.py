"""
  仿照fork多进程并发逻辑，编写具有同样功能的多线程并发程序
"""
from threading import Thread
import os
from socket import *
s= socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)#端口重复使用
s.bind(('0.0.0.0',8887))
s.listen(3)
print("Listen the port 8888...")

def handle(c):
    while True:
        data = c.recv(1024)
        if not data.decode():
            break
        print(data.decode())
        c.send(b'ok')
    c.close()

while True:
    try:
        c,addr = s.accept()
        print("Connect from ",addr)
    except KeyboardInterrupt:
        os._exit(0)
    except Exception as e:
        print(e)
        continue
    t = Thread(target=handle,args=(c,))
    t.setDaemon(True) # 分支线程随主线程退出
    t.start()


