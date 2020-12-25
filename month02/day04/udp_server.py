"""
   udp_server.py   udp服务端流程
   重点代码
"""
#创建udp套接字
from socket import  *
sockfd=socket(AF_INET,SOCK_DGRAM)
#绑定地址
sockfd.bind(('127.0.0.1',9999))
print("等待消息")
#收发消息
while True:
    data,addr=sockfd.recvfrom(1024)
    print("收到来自%s的消息:%s"%(addr,data.decode()))
    sockfd.sendto(b'ok',addr)
#关闭套接字
sockfd.close()