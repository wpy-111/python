"""
   练习：
       在终端中循环录入学生信息（名字，年龄，成绩，性别）
       ----创建学生类
       ----打印个人信息
"""


class Student:
    def __init__(self, name, old, achement, gender):
        self.name = name
        self.old = old
        self.achement = achement
        self.gender = gender
    def print_personal_info(self):
        print("学生姓名：", self.name, "年龄：", self.old, "成绩：", self.achement, "性别：", self.gender)
list_student=[]
while True:
    name01=input("请输入学生姓名:")
    if name01=="":
        break
    old01=int(input("请输入学生年龄："))
    achement01=int(input("请输入学生成绩："))
    gender01=input("请输入学生性别：")
    stu=Student(name01,old01,achement01,gender01)
    list_student.append(stu)
for item in list_student:
    item.print_personal_info()