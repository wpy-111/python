"""
   非阻塞IO
"""
from socket import *
from time import sleep,ctime
#创建套接字
s = socket()
s.bind(('127.0.0.1',8888))
s.listen(3)
#设置非阻塞  False是非阻塞   Ture是阻塞
s.setblocking(False)

#设置超时时间
s.settimeout(2)
while True:
    print("Waiting for connect....")
    sleep(10)
    c,addr = s.accept()
    #c也可以设置非阻塞   c.setblocking（False）