"""
    tcp_client1.py 客户端
"""
from socket import *
#1.创建tcy套接字
sockfd=socket()
#2.连接服务器
server_adder=('127.0.0.1',8888)
sockfd.connect(server_adder)
print("连接成功")
while True:
    data=input("mag>>")
    if not data:
        break
    sockfd.send(data.encode())
    date=sockfd.recv(1024)
    print("From server:",date.decode())
sockfd.close()
#3.发送给服务端  必须是字节串
#4.关闭套接字
