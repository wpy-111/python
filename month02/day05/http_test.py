"""
   获取http的请求
   回复响应
"""
from socket import *
#http使用tcp协议
s=socket()
s.bind(('0.0.0.0',8001))
s.listen(5)
c,addr=s.accept()
print("Connect from",addr)
request=c.recv(4086)
print(request.decode())
response="""http/1.1 200 ok
Content-type:text/html;charset=UTF-8

hello python 我爱你.
"""
c.send(response.encode())
c.close()
s.close()