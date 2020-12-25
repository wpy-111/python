from socket import *
ADDR=('127.0.0.1',7777)
s=socket(AF_INET,SOCK_DGRAM)
while True:
    message=input(">>")
    if not message:
        break
    s.sendto(message.encode(),ADDR)
    data,addr=s.recvfrom(1024)
    print("单词解释:%s" % data.decode())
s.close()