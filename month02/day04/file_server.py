"""
练习
    选择一张图片，在客户端上传到服务端
    温馨提示：
             客户端读取图片的内容
             将内容发送给服务端
             服务端接受照片内容
             保存在服务端的某个位置
"""
SAVE_PATH='/home/tarena/图片/'
from socket import *
from  time  import localtime
s=socket()
s.bind(('127.0.0.1',6666))
s.listen(3)
print("Waiting for connect..")
connfd,addr=s.accept()
print("Connect from",addr)
itm="%s-%s-%s"%localtime()[:3]
c=open(SAVE_PATH+itm,'wb')
while True:
    data=connfd.recv(1024)
    if not data:
        break
    c.write(data)
c.close()
s.close()
connfd.close()
