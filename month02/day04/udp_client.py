"""
   udp_client.py   udp客户端流程
   重点代码
"""
#打开udp套接字
ADDR=('127.0.0.1',9999)
from socket import *
sockfd=socket(AF_INET,SOCK_DGRAM)
#循环发送消息
while True:
    message=input(">>")
    if not message:
        break
    sockfd.sendto(message.encode(),ADDR)
    data,addr=sockfd.recvfrom(1024)
    print("From server:%s"%data)
sockfd.close()