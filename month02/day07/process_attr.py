"""
   进程属性
"""
from multiprocessing import Process
import  time
#设计daemon属性，在start之前
#随着父进程的结束，子进程也随之结束
