class Student:
    def __init__(self, name, old, achement, gender):
        self.name = name
        self.old = old
        self.achement = achement
        self.gender = gender

    def print_personal_info(self):
        print("学生姓名：", self.name, "年龄：", self.old, "成绩：", self.achement, "性别：", self.gender)

list_student = [
    Student("悟空", 27, 100, "男"),
    Student("八戒", 30, 60, "男"),
    Student("沙僧", 33, 70, "男"),
    Student("唐僧", 20, 65, "女")
]


# 1.定义函数，在学生列表中查找姓名是八戒的学生对象
# 测试，将对象打信息打印在终端中
def find_bajie():
    for item in list_student:
        if item.name == "八戒":
            return item


stu = find_bajie()
if stu:
    stu.print_personal_info()


# 2.定义函数，在学生列表中查找成绩大于60的学生所有对象
# 测试，将所有对象打信息打印在终端中
def find_than60():
    list_result = []
    for item in list_student:
        if item.achement > 60:
            list_result.append(item)
    return list_result


for item in find_than60():
    item.print_personal_info()


# 3.定义函数，在学生列表中查找所有年龄大于30的学生姓名
# 测试，将所有名字打印在终端中
def find_old_than30_name():
    list_result = []
    for item in list_student:
        if item.old > 30:
            list_result.append(item.name)
    return list_result
for i in find_old_than30_name():
    print(i)
# 4.定义函数，在学生列表中查找成绩最低的学生对象
# 测试，将该学生的信息打印在终端中
def find_most_low_achement_student():
    most_low_achement_student=list_student[0]
    for item in range(1,len(list_student)):
        if most_low_achement_student.achement>list_student[item].achement:
            most_low_achement_student = list_student[item]
    return most_low_achement_student
find_most_low_achement_student().print_personal_info()
#     most_low_achement = list_student[0].achement
#     for item in list_student[1:]:
#         if most_low_achement> item.achement:
#             most_low_achement = item.achement
#     return most_low_achement
# find_most_low_achement_student()
# for item in list_student:
#     if item.achement==find_most_low_achement_student():
#         item.print_personal_info()
