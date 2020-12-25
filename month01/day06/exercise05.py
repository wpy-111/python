"""
   练习:在终端中录入录入多个学生的信息,(名字,年龄,成绩,性别)
   如果录入空格停止
   ---将所有学生信息打印出来(一行一个)
   ----如果录入赵敏则单独打印其信息
"""

dict={}
while True:
    name=input("请输入学生姓名:")
    if name==" ":
        break
    old=int(input("请输入学生年龄:"))
    achement=float(input("请输入学生成绩:"))
    gender=input("请输入学生性别:")
    if name not in dict:#字典里面包含列表
        dict[name]=[old,achement,gender]
if "赵敏"in dict:
    print("赵敏的年龄是%d,成绩是%f,性别%s"%(dict["赵敏"][0],dict["赵敏"][1],dict["赵敏"][2]))
for key,value in dict.items():
    print("%s的年龄是%d,成绩是%f,性别%s."%(key,value[0],value[1],value[2]))
