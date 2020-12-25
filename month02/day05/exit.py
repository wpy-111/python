"""
   exit.py 进程结束
"""
import os
import sys
#父子进程退出互相不受影响
sys.exit('退出进程')
# os._exit(0)
# print("exit process")