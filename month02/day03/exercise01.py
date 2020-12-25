"""
   编写一个程序，向一个文件（log.txt）中不断写入内容
   要求每两秒写入一行
"""
import time
f=open('log.txt','a+')
n=0
f.seek(0)
for line in f:
    n+=1
while True:
    time.sleep(2)
    n+=1
    s="%d.%s\n"%(n,time.strftime("%Y年%m月%d日%H时%M分%S秒",time.localtime()))
    f.write(s)
    f.flush()


