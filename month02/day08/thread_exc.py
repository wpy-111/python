"""
  使用多个线程，同时从多个地方拷贝文件的某一部分
  最终在本地合并为一个
提示：1.判断哪些目录下有目标文件
      2.有几个路径下有，就创建几个线程
      3.每个线程负责一个路径，要选好下载文件的哪部分
      4.多个线程下载的内容需要为一个文件
"""

usl = ['/home/tarena/桌面/',
       '/home/tarena/模板/',
       '/home/tarena/音乐/',
       '/home/tarena/图片/',
       '/home/tarena/下载/',
       '/home/tarena/视频/']
from threading  import Thread,Lock
import os
file_name = input("file:")
file = []
for i in usl:
    if os.path.exists(i+file_name):
        file.append(i+file_name)
path_number = len(file)
print(path_number)
if path_number == 0:
    print("无资源")
    os._exit(0)
file_size = os.path.getsize('/home/tarena/桌面/桌面.jpg')#文件大小
print(file_size)
#本地文件打开要储存的新位置
s = open('file01.jpg','ab')
n = 0
def write_file(item):
    global n
    c=open(item,'rb')
    c.seek(n,1)
    s.write(c.read(int(file_size//path_number+1)))
    n += file_size//path_number+1
    c.close()

list_file = []
for item in file:
    t = Thread(target=write_file,args=(item,))
    t.start()
    list_file.append(t)
for item in list_file:
    item.join()
s.close()

