"""
    创建学生类（姓名，年龄，成绩）
    直接将学生对象输出到终端
    print（学生信息）
    将学生对象克隆一份，改变其中一个的信息，打印另一个的信息
"""
class Student:
    def __init__(self, name="", old=0, score=0):
        self.name=name
        self.old=old
        self.score=score
    def __str__(self):
        return "我是%s，今年%d岁，成绩是%d"%(self.name,self.old,self.score)
    def __repr__(self):
        return  'Student("%s","%d","%d")'%(self.name,self.old,self.score)
s01=Student("小王",12,100)
print(s01.__str__())
#克隆复制一个s02 和s01完全相等    （ 用__repr__  和eval 进行克隆）
s02=eval(s01.__repr__())
s01.name="小赵"
print(s02.name)
print(s01.name)