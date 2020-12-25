"""
   ftp文件服务  客户端
"""
from socket import *
class FTPClient:
    def __init__(self,s):
        self.s=s
    def ftp_list(self):
        self.s.send(b'L')  # 发送请求
        data = self.s.recv(128).decode()
        print(data)
        if data == 'ok':
            date = self.s.recv(1024*1024*10).decode()
            print(date)
        else:
            print(data.decode())
    def download(self,file_name):
        data = "G "+file_name
        self.s.send(data.encode())
        data = self.s.recv(128).decode()
        if data == 'ok':
            f = open(file_name,'wb')
            while True:
                data = self.s.recv(1024)
                if data == b'##':
                    break
                f.write(data)
            f.close()
        else:
            print(data)

def main():
    s = socket()
    s.connect(('127.0.0.1', 8080))
    ftp = FTPClient(s)
    while True:
        print('******** 命令 **********')
        print('*******   L   *********')
        print('*******   P filename **')#上传
        print('*******   G filename **')#下载
        print('*******   Q   *********') #退出
        cmd = input("命令：")
        if cmd == 'L':
            ftp.ftp_list()
        elif cmd[0] == 'P':
            pass
        elif cmd[0] == 'G':
            file_name=cmd.split(' ')[-1]
            ftp.download(file_name)
        else:
            print("输入命令错误")


if __name__ == '__main__':
    main()

