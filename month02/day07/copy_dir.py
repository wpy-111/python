"""
 使用进程池去备份一个目录，该目录包含若干个普通文件
     提示：
         os.listdir（）
         os.path.getsize（）
         os.mkdir（）创建一个目录
* 至少拷贝四个文件，并且仅能创建四个进程
   拷贝过程时时打印百分比
"""
from multiprocessing import Pool,Queue
import os
import time
queue = Queue()
size = 0
for item in os.listdir('../day04'):
    size += os.path.getsize('../day04/'+item)
def copy(i):
    c = open('../day04/'+i,'rb')
    b = open('/home/tarena/wpy/123/'+i,'wb')
    n=b.write(c.read())
    queue.put(n)
    c.close()
    b.close()

pool = Pool(4)
for file in os.listdir('../day04'):
    pool.apply_async(func=copy,args=(file,))
pool.close()
print('文件总大小：%.2f M'%(size/1024/1024))
size01 = 0
while size01 < size:
    size01 += queue.get()
    print('拷贝了%.1f%%'%(size01/size*100))

pool.join()
