"""
    练习：
        使用udp编程完成
        从客户端循环录入单词，获得单词解释
        服务端提供这个解释
"""
SAVE_PATH='/home/tarena/dict.txt'
from socket import *
s=socket(AF_INET,SOCK_DGRAM)
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(('127.0.0.1',7777))
print("等待消息")
def find_world(data):
    c = open(SAVE_PATH, 'rb')
    for line in c:
        if line.decode().split(" ")[0] > data.decode():
            c.close()
            return "没有该单词"
        elif data.decode() == line.decode().split(' ')[0]:
            c.close()
            return s.sendto(line, addr)
    else:
        c.close()
        return "没有该单词"
while True:
    data,addr=s.recvfrom(1024)
    print("收到来自%s的单词:%s"%(addr,data.decode()))
    find_world(data)
#关闭套接字
