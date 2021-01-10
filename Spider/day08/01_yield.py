"""
yield关键字作用：
   1.当一个函数中有了yield语句，当做生成器来使用
   2.函数会在yield的位置暂停pause，下次调用时会接着进行
   3.yield是实现协程的关键字，协程又称微线程
"""
def f1():
    for i in range(1,3):
        yield 1



g = f1()
print(next(g))
print(next(g))













