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


# 5.根据年龄，并按照升序将学生列表进行排序
def ascending():
    for i in range(0, len(list_student) - 1):
        for m in range(i + 1, len(list_student)):
            if list_student[i].old > list_student[m].old:
                list_student[i], list_student[m] = list_student[m], list_student[i]

ascending()
for item in list_student:
    item.print_personal_info()

# 6.将学上列表中所有男生删除
def del_nan():
    for item in list_student[::-1]:
        if item.gender=="男":
            list_student.remove(item)
del_nan()
for i in list_student:
    i.print_personal_info()