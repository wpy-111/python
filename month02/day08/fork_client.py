from socket import *
import os
Host='127.0.0.1'
PORT = 8887
ADDR=(Host,PORT)
s = socket(AF_INET,SOCK_STREAM)
s.connect(ADDR)
while True:
    data = input("Mess>>")
    s.send(data.encode())
    date = s.recv(1024)



