from socket import *
import os,sys
"""
"""
#服务地址
ADDR=('0.0.0.0',8888)
user = {}
bad={}
blacklist=[]
#启动函数
def main():
    sockfd=socket(AF_INET,SOCK_DGRAM)
    sockfd.bind(ADDR)
    pid=os.fork()
    if pid < 0:
        return
    elif pid ==0:
        #实现管理员权限
        while True:
            txt=input("管理员消息：")
            mes="C 管理员 ：%s"%txt
            sockfd.sendto(mes.encode(),ADDR)

    else:
        do_request(sockfd)
#进入处理
def do_login(sockfd,name,addr):
    if name in user or '管理' in name or addr in blacklist:
        return sockfd.sendto(b'FAIL',addr)
    sockfd.sendto(b'OK',addr)
    #通知其他人
    mes="\n欢迎%s进入聊天室"%name
    for i in user:
        sockfd.sendto(mes.encode(),user[i])
    #将其添加到字典中
    user[name]=addr
    bad[name]=0
#功能分发函数
def handle_mes(name,content,sockfd):
    mes='\n%s:%s'%(name,content)
    if "xx"in mes:
        sockfd.sendto("\n管理员：含有敏感词汇注意".encode(),user[name])
        bad[name] +=1
        blacklist.append(user[name])
        if bad[name] == 3 :
            sockfd.sendto("\n管理员：你以被提出群聊".encode(), user[name])
            del user[name]
            del bad[name]
            mes = "\n%s由于不良行为已被提出群聊"%name
            for i in user:
                sockfd.sendto(mes.encode(), user[i])
            sockfd.sendto(b'EXIT' ,user[name])
        return
    for i in user:
        if i != name:
            sockfd.sendto(mes.encode(),user[i])

def do_quit(sockfd,name):

    mes='\n%s退出群聊'%name
    for i in user:
        if name != i:
            sockfd.sendto(mes.encode(),user[i])
        else:
            sockfd.sendto(b'EXIT',user[i])
    del user[name]

def do_request(sockfd):
    while True:
        data,addr = sockfd.recvfrom(128)
        tmp=data.decode().split(' ',2)
        #根据不同的请求类型选择不同功能模块去处理
        # L C Q
        if tmp[0] == "L":
            do_login(sockfd,tmp[1],addr)
        elif tmp[0] == "C":
            handle_mes(tmp[1],tmp[2],sockfd)
        elif tmp[0] == "Q":
            do_quit(sockfd,tmp[1])

if __name__ == '__main__':
    main()

