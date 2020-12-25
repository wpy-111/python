"""
   练习:在终端中录入录入多个学生的信息,(名字,年龄,成绩,性别)
   如果录入空格停止
   ---将所有学生信息打印出来(一行一个)
   ---打印最后一个学生信息(列表有顺序,字典无顺序)
   总结:字典与列表的实用性
   列表:优点:获取数据更为灵活(索引/切片)
           节省内存(顺序排列)
       缺点:查找某个元素相对较慢(从头依次开始)
           代码可读性相对较高(根据索引/切片获取)----解决方案  list存储一类信息
    字典:优点:根据键查找值速度最快
             代码可读性相对较高(key的名字)
        缺点: 获取数据不灵活
             占用内存过多(分散排列)
"""
list_result=[]
while True:
    name = input("请输入学生姓名:")
    if name == " ":
        break
    old = int(input("请输入学生年龄:"))
    achement = float(input("请输入学生成绩:"))
    gender = input("请输入学生性别:")
    dict = {"姓名": name, "年龄": old, "成绩": achement, "性别": gender}
    if dict not in list_result:#列表里面包含字典
        list_result.append(dict)
for i in list_result:
    print("%s的年龄是%d,成绩是%d,性别是%s"%(i["姓名"],i["年龄"],i["成绩"],i["性别"]))
# print(list01[-1])
last_dict=list_result[-1]
print("%s的年龄是%d,成绩是%d,性别是%s"%(last_dict["姓名"],last_dict["年龄"],last_dict["成绩"],last_dict["性别"]))