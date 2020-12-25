"""
   练习：
   编写一个服务端http程序，在客户段发起request请求时
   将网页按照http响应格式发送给浏览器显示
   温馨提示：
           网页内容是响应体，注意协调响应格式
           对请求做一定的判断，如果请求是/发送这个网站
           如果是其他则用404回应
"""

from socket import *
#http使用tcp协议
sockfd=socket()
sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
sockfd.bind(('0.0.0.0',8000))
sockfd.listen(5)

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

while True:
    try:
        connfd,addr=sockfd.accept()
    except KeyboardInterrupt:
        break
    handel(connfd)
sockfd.close()

