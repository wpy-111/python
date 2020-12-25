"""
  select.server.py
  重点代码
【1】将关注的IO放入对应的监控类别列表
【2】通过select函数进行监控
【3】遍历select返回值列表，确定就绪IO事件
【4】处理发生的IO事件
"""
from socket import *
from select import select

s = socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)#重复使用端口
s.bind(('127.0.0.1',8888))
s.listen(3)
#设置列表
rlist = [s]#关注s的读IO事件
wlist = []
xlist = []

#监循环控IO对应的事件发生
while True:
    rs,ws,xs = select(rlist,wlist,xlist)
    for item in rlist:
        if item is s:
            c,addr = item.accept()
            rlist.append(c)
            print("Connect From",addr)
        else:
            print("接受信息",item.getpeername())
            data = item.recv(1024).decode()
            if not data:
                continue
            print(data)
            item.send(b'ok')