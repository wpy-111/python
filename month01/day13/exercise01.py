"""
   继承
"""
class Preson:
    def say(self):
        print("说话")
class Student(Preson):
    def study(self):
        print("学习")
class Teacher(Preson):
    def speake(self):
        print("讲课")
s01=Student()
t01=Teacher()
p01=Preson()
#继承的内置函数
# 学生对象是一种学生类型
print(isinstance(s01,Student))#True
# 人对象是一种学生类型
print(isinstance(p01,Student))#False
# 学生对象是一种人类型
print(isinstance(s01,Preson))#True
# 学生类型是学生类型
print(issubclass(Student,Student))#True
# 学生类型是人类型
print(issubclass(Student,Preson))#True
# 人类型是学生类型
print(issubclass(Preson,Student))#False

