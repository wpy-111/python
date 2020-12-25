"""
   学生信息管理系统
"""
class StudentModel:
    def __init__(self, name="", old=0, score=0, id=0):
        self.name = name
        self.old = old
        self.score = score
        self.id = id
class StudentManagerController:
    init_id = 1000
    def __init__(self):
        self.__stu_list = []
    @property
    def stu_list(self):
        return self.__stu_list
    def add_student(self, stu_target):
        self.__generate_id(stu_target)
        self.__stu_list.append(stu_target)
    def __generate_id(self, stu_target):
        StudentManagerController.init_id += 1
        stu_target.id = StudentManagerController.init_id
    def remove_student(self,stu_id):
        for item in self.stu_list:
            if item.id==stu_id:
                self.stu_list.remove(item)
                return True
        return False
    def update_student(self,stu_tareget):
        for item in self.stu_list:
            if item.id==stu_tareget.id:
                item.name=stu_tareget.name
                item.old=stu_tareget.old
                item.score=stu_tareget.score
                return  True
        return  False
    def order_by_score(self):
        for i in range(0,len(self.stu_list)-1):
            for c in range(i+1,len(self.stu_list)):
                if self.stu_list[i].score >self.stu_list[c].score:
                    self.stu_list[i],self.stu_list[c]=self.stu_list[c],self.stu_list[i]
class StudentManagerView:
    def __init__(self):
        self.__controller=StudentManagerController()
    def __display_menu(self):
        print("1)添加学生")
        print("2)显示学生信息")
        print("3)删除学生")
        print("4)修改学生")
        print("5)根据学生成绩升序显示学生")
    def __select_menu(self):
        item = input("请输入选项：")
        if item =="1":
            self.__input_student()
        elif item =="2":
            self.__output_student()
        elif item =="3":
            self.__delete_student()
        elif item =="4":
            self.__modify_student()
        elif item =="5":
            self.__output_student_by_score()

    def main(self):
        while True:
            self.__display_menu()
            self.__select_menu()

    def __input_student(self):
        while True:
            name=input("请输入姓名：")
            if name =="":
                break
            old=int(input("请输入年龄："))
            score=float(input("请输入分数："))
            stu=StudentModel(name,old,score)
            self.__controller.add_student(stu)

    def __output_student(self):
        for item in self.__controller.stu_list:
            print(item.id,item.name,item.old,item.score)

    def __delete_student(self):
        id = int(input("请输入删除id："))
        if self.__controller.remove_student(id):
            print("删除成功")
        else:
            print("删除失败")

    def __modify_student(self):
        id = int(input("请输入学生编号："))
        name = input("请输入修改的姓名：")
        old = int(input("请输入修改的年龄："))
        score = float(input("请输入修改的分数："))
        stu = StudentModel(name, old, score,id)
        self.__controller.update_student(stu)

    def __output_student_by_score(self):
        self.__controller.order_by_score()
        self.__output_student()

view=StudentManagerView()
view.main()
# manager = StudentManagerController()
# stu01 = StudentModel("悟空", 15, 100)
# stu02 = StudentModel("赵敏", 10, 62)
# stu04 = StudentModel("小王", 20, 88)
# stu05 = StudentModel("小张", 25, 60)
# stu03 = StudentModel("武帝", 30, 72,1001)
# manager.add_student(stu01)
# manager.add_student(stu02)
# manager.add_student(stu04)
# manager.add_student(stu05)
# re=manager.update_student(stu03)
# print(re)
# # rw=manager.remove_student(1002)
# # print(rw)
# manager.order_by_score()
# for item in manager.stu_list:
#     print(item.id, item.name,item.score)
