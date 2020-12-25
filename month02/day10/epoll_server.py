from select import *
from socket import *
s = socket()
ADDR=('127.0.0.1',8887)
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(ADDR)
s.listen(3)
#创建epoll对象
ep = epoll()
ep.register(s,EPOLLIN)#将s设置关注

#建立一个字典，用于通过文件描述符来查找对应的IO
#跟关注的IO保持一致
fdmap={s.fileno():s}
#循环监控IO
while True:
    events = ep.poll()#阻塞等待IO的发生
    for fd,event in events:
        #if 结构区分哪个IO准备就绪 fd -fileno   event-IO类别
        if fd == s.fileno():
            c,addr= fdmap[fd].accept()
            print("Connect From  ",addr)
            ep.register(c,EPOLLIN)#关注客户端套解字
            fdmap[c.fileno()]=c
        else:
            data = fdmap[fd].recv(1024).decode()
            if not data:
                #p.unregister(fd) 功能：取消对IO的关注
                # 参数：IO对象或者IO对象的fileno
                ep.unregister(fd)
                fdmap[fd].close()
                del fdmap[fd]  #删除该套解字
                continue
            print(data)
            fdmap[fd].send(b'ok')

