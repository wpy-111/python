"""
   tcp.server.py  服务端   socket 套接字
"""
import socket
#1.创建tcp套接字（流式套接字）  地址类型  套接字的类型
#2.绑定地址  bind 的参数是元祖
#3.设置监听  参数是监听的大小
#4.处理客户端连接******
# connfd  客户端连接套接字
# addr    连接的客户端地址
# 5.收发消息  必须是字节串
# 6.关闭套接字
sockfd=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sockfd.bind(('0.0.0.0',8888))
sockfd.listen(5)
while True:
    print("正在请求连接")
    connfd,addr=sockfd.accept()
    print("连接到"+str(addr))
    while True:
        data=connfd.recv(1024)
        if not data:
            break
        print(data.decode())
        n=connfd.send("你好".encode())
        print("Send %d bytes"%n)
    connfd.close()
sockfd.close()