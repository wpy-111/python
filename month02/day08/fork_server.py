"""
   基于fork的多进程服务
   重点代码
"""
from socket import *
import os
import signal
Host='0.0.0.0'
PORT = 8888
ADDR=(Host,PORT)
s = socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)#端口重复使用
s.bind(ADDR)
s.listen(3)
print("Listen the port 8888...")

#处理僵尸进程signal
#signle在子进程前设置
signal.signal(signal.SIGCHLD,signal.SIG_IGN)

def handle(c):
    while True:
        data = c.recv(1024)
        if not data:
            break
        print(data.decode())#变成字符串
        c.send(b'ok')
    c.close()

while True:
    #循环接受
    try:
        c,addr=s.accept()
        print("Connect from ",addr)
    except KeyboardInterrupt:
        os._exit(0)
    except Exception as e:
        print(e)
        continue
        #客户端连接处理
    pid = os.fork()
    if pid == 0:
        handle(c)#处理请求
        os._exit(0)#退出子进程


