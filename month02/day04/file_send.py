from socket import *
s=socket()
s.connect(('127.0.0.1',6666))
message=input("》")
c=open(message,'rb')
while True:
    data=c.read(1024)
    if not data:
        break
    s.send(data)
s.close()
c.close()