"""
     练习：
          创建三种方式，调用当前模块的成员fun01,fun02,fun03
"""
def fun01():
    print("module01 -- fun01")
class MyClass:
    def __init__(self, hp=0):
        self.hp=hp
    def fun02(self):
        print("module01 -- fun02")
    @classmethod
    def fun03(cls):
        print("module01 -- fun03")