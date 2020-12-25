"""
   http_server v2.0.py
   io多路复用和http
"""
from socket import *
from  select import *

class HTTPSever:
    def __init__(self,host,port,dir):
        self.host = host
        self.port = port
        self.dir = dir
        self.addr=(host,port)
        self.creat_sockfed()

    def creat_sockfed(self):
        self.sockfed = socket()
        self.sockfed.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
        self.sockfed.bind(self.addr)
    def handle(self,data):
        pass
    def server_fover(self):
        self.sockfed.listen(3)
        print("Listen the port %d"%self.port)
        #IO多路复用循环接听 客户端请求
        rlist = [self.sockfed]
        wlist = []
        xlist = []
        while True:
            rs,ws,xs = select(rlist,wlist,xlist)
            for item in rs:
                if item is self.sockfed:
                    c,addr = self.sockfed.accept()
                    print("Connect From ",addr)
                    rs.append(c)
                else:
                    print("接受信息",item.getpeername())
                    data = item.recv(1024).decode()
                    request_line = data.split('\n')[0]
                    request_content = request_line.split(" ")[1]
                    if request_content == '/'or request_line[-5]=='.html':
                        response = self.get_html(item,request_content)
                    else:
                        response = "HTTP/1.1 200 OK\r\n"
                        response += "Content-type:text/html\r\n"
                        response += "\r\n"
                        response += "<h1> woaini </h1>"
                    item.send(response.encode())

    def get_html(self,connefd,info):
        if info == '/':
            filename =self.dir + '/Linux.html'
        else:
            filename = self.dir + info
        try:
            f = open(filename,'r')
        except:
            #网页不存在
            response = "HTTP/1.1 404 Not Found\r\n"
            response += "Content-type:text/html\r\n"
            response += "\r\n"
            response +="Sorry...."
        else:
            response = "HTTP/1.1 200 ok\r\n"
            response += "Content-type:text/html\r\n"
            response += "\r\n"
            response += f.read()
            #网页存在
        finally:
            #将结果发送个浏览器
            connefd.send(response.encode())


if __name__ == '__main__':
    port=8888
    host='0.0.0.0'
    dir = './static'#  网页位置
    http = HTTPSever(host,port,dir)
    http.server_fover()