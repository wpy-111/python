"""
   练习：利用http——server.py程序，编写一个fork多进程程序，
        让用户可以通过8000端口访问端应用也可以通过8080端口访问后端应用
"""

from socket import *
import os,time
#http使用tcp协议
def handel(connfd):
    request=connfd.recv(1024).decode()
    request_line=request.split("\n")[0]
    request_content=request_line.split(" ")[1]
    if request_content=='/':
        response = "HTTP/1.1 200 ok\r\n"
        response += "Content-type:text/html\r\n"
        response += "\r\n"
        with open('index.html') as f:
            response += f.read()
    else:
        response = "HTTP/1.1 404 NOTFOUND\r\n"
        response += "Content-type:text/html\r\n"
        response += "\r\n"
        response += "sorry...."
    connfd.send(response.encode())

def main(port):
    sockfd = socket()
    sockfd.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    sockfd.bind(('0.0.0.0', port))
    sockfd.listen(5)
    while True:
        try:
            connfd, addr = sockfd.accept()
        except KeyboardInterrupt:
            break
        handel(connfd)
    sockfd.close()

pid=os.fork()
if pid<0:
    print("Creat process failed")
elif pid == 0:
    main(8000)
else:
    main(8080)


