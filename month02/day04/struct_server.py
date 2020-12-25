"""
  作业：
       使用udp和struct完成
       1.从客户端循环录入学生信息
       信息包括：id 姓名 年龄 身高
       2.信息打包发给服务端
       3.在服务端将学生信息写入到一个文件中，每个学生信息占一行
"""
SAVE_PATH='/home/tarena/wpy/lvze/day04/file'
from socket import *
from struct import *
s=socket(AF_INET,SOCK_DGRAM)
s.bind(('127.0.0.1',8888))
c=open(SAVE_PATH,'w')
st=Struct('i32sif')
while True:
    data,addr=s.recvfrom(1024)
    mes=st.unpack(data)
    id,name,height,score=mes
    name=name.decode().strip('\x00')
    c.write('学生id：%d，学生姓名：%s，学生身高：%d，学生成绩：%f\n'%(id,name,height,score))
    c.flush()