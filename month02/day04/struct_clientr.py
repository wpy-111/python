from socket import *
from struct import *
ADDR=('127.0.0.1',8888)
s=socket(AF_INET,SOCK_DGRAM)
st = Struct('i32sif')
while True:
    id=int(input("学生id："))
    if not id:
        break
    name=input("学生姓名：")
    height=int(input("学生身高："))
    score=float(input("学生成绩："))
    data=st.pack(id,name.encode(),height,score)
    print('打包成功')
    s.sendto(data,ADDR)
s.close()