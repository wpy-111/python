"""
   ftp 文件处理
   多线程并发
"""
from threading import Thread
from socket import *
import os,sys
from time import sleep
#全局变量
HOST = '0.0.0.0'
PORT = 8080
ADDR = (HOST,PORT)
FTP = '/home/tarena/wpy/FTP'#文件库位置
#实现文件传输的具体功能
class FTPserver(Thread):
    def __init__(self,c):
        self.c = c
        super().__init__()
    def run(self):
        data =self.c.recv(1024).decode()
        if data == 'L':
            self.do_list()
        elif data.split(' ')[0] == 'G':
            file_name = data.split(' ')[-1]

            self.do_download(file_name)
    #文件列表发送
    def do_list(self):
        file_list = os.listdir(FTP)
        if not file_list:
            self.c.send('没有文件'.encode())
            return
        else:
            self.c.send(b'ok')
            sleep(0.1)
        data = '\n'.join(file_list)
        self.c.send(data.encode())
    #文件下载
    def do_download(self, file_name):
        try:
            b = open(FTP+'/'+file_name,'rb')
        except Exception:
            self.c.send('文件不存在'.encode())
            return
        else:
            self.c.send(b'ok')
            sleep(0.1)
        while True:
            data = b.read(1024)
            if not data:
                sleep(0.1)
                self.c.send(b'##')
                break
            self.c.send(data)
        b.close()


#搭建网络模型
def main():
    s = socket()
    s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)  # 端口重复使用
    s.bind(ADDR)
    s.listen(3)
    print("Listen the port 8888...")
    while True:
        try:
            c,addr = s.accept()
            print("Connect from ", addr)
        except KeyboardInterrupt:
            os._exit(0)
        except Exception as e:
            print(e)
            continue
        c=FTPserver(c)
        c.start()
if __name__ == '__main__':
    main()
