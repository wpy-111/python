"""
    global 用法
    调用函数
"""

def add():
    global a
    a =100
def b():
    a+10
    print(a)
