"""
   从多处使用线程同时下载文件练习
   *文件资源库从本地目录变为 网络地址address
   *多线程从网络中获取文件，在本地下载1个
"""
usl = ['/home/tarena/桌面/',
       '/home/tarena/模板/',
       '/home/tarena/音乐/',
       '/home/tarena/图片/',
       '/home/tarena/下载/',
       '/home/tarena/视频/']
FTP='/home/tarena'
from threading  import Thread,Lock
import os
from socket import *
class FerServer(Thread):
    def __init__(self,c):
        super().__init__()
        self.c = c
    def run(self):
        while True:
            data = self.c.recv(128)
    def dowload(self,filename):
        try:
            open(FTP,'wb')
        except Exception as e:
            print(e)


def main():
    s =socket()
    s.bind(('127.0.0.1',8888))
    s.listen(3)
    print("listen the port 8080...")
    while True:
        try:
            c, addr = s.accept()
            print("Connect from ", addr)
        except KeyboardInterrupt:
            os._exit(0)
        except Exception as e:
            print(e)
            continue
        t = FerServer(c)
        t.start()



