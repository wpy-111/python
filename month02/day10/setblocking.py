from threading import Thread
from socket import *
import os,sys
from time import sleep
"""
    sockfet.set.blocking(False)  设置非阻塞IO
    默认为True，表示套接字IO阻塞；设置为False则套接字IO变为非阻塞
    超时检测 sockfed.settimeout(sex)
    设置一个最长阻塞时间，超过该时间后则不再阻塞等待
"""
HOST = '0.0.0.0'
PORT = 8080
ADDR = (HOST,PORT)
FTP = '/home/tarena/wpy/FTP'#文件库位置
#实现文件传输的具体功能

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

if __name__ == '__main__':
    main()
