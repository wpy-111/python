from multiprocessing import Pool
from time import sleep,ctime
def fun(mes):
    sleep(2)
    print(ctime(),mes)
    return 8888
pool = Pool(4)
#向进程池中添加事件
for i in range(10):
    mes = 'neba%d'%i
    #r是返回函数事件的返回值
    r = pool.apply_async(func=fun,args=(mes,))
#关闭进程池
pool.close()
#回收进程，父进程等待子进程一同完成
pool.join()
#获取进程事件的返回值
print(r.get())