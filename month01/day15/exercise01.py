"""
    调用module01的方法
"""
import module01
module01.fun01()
s01=module01.MyClass()
s01.fun02()
module01.MyClass().fun03()
from module01 import fun01
fun01()
from module01 import MyClass
MyClass().fun02()
from module01 import *
fun01()
c01=MyClass()
c01.fun02()
MyClass().fun03()
