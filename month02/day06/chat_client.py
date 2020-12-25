"""
    chat room client
"""
from socket import *
import os,sys
#客户端启动函数
ADDR=('127.0.0.1',8888)

def send_message(sockfd,name):
    while True:
        try:
            data=input("请输入发送的内容：")
        except KeyboardInterrupt:
            mes = 'Q ' + name
            sockfd.sendto(mes.encode(), ADDR)
            sys.exit('\n退出群聊')
        #退出
        if data =="quit":
            mes='Q '+name
            sockfd.sendto(mes.encode(),ADDR)
            sys.exit('退出群聊')
        mes='C %s %s'%(name,data)
        sockfd.sendto(mes.encode(),ADDR)

def recv_message(sockfd):
    while True:
        try:
            data,addr=sockfd.recvfrom(128)
        except KeyboardInterrupt:
            sys.exit('退出聊天室')
        if data == b'EXIT':
            sys.exit('退出聊天室')
        print(data.decode(),"\n请输入发送的内容：",end=" ")

def main():
    sockfd=socket(AF_INET,SOCK_DGRAM)
    # 进入聊天wpl室
    while True:
        name=input("请输入姓名：")
        message = "L "+name
        sockfd.sendto(message.encode(),ADDR)
        #得到结果
        data,addr=sockfd.recvfrom(128)
        if data.decode() == 'OK':
            print("您已进入聊天室")
            break
        else:
            print("进入聊天室失败")
    #收发消息
    pid = os.fork()
    if pid < 0 :
        return "系统崩溃"
    elif pid == 0:
        send_message(sockfd,name)
    else:
        recv_message(sockfd)

if __name__ == '__main__':
    main()