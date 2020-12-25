"""
    练习：
    定义员工管理器
    1.储存所有员工
    2.提供计算总薪资的方法
    普通员工：底薪
    程序员：底薪+项目分红
    测试员：底薪+Bug数*5
"""
# 封装，继承，多态
# 开闭：增加新员工，不改变员工管理器
# 单一：员工管理器（记录，总薪资），程序员（计算薪资），测试员
# 依赖倒置：员工管理调用普通员工（父）不调用具体员工（子）
# 组合复用：员工管理器和具体员工是组合关系
# 里氏替换：storage_staff参数是普通员工，传递是具体员工
#          具体员工重写时，调用了父亲n计算薪资的方法（扩展重写）
# 迪米特：员工管理器，程序员，测试员（低藕合）
class Staff_Manager:
    def __init__(self):
        self.__list_staff = []
    def storage_staff(self,starget):
        self.__list_staff.append(starget)
    def calculate_all_salary(self):
        sum_salary=0
        for item in self.__list_staff:
            sum_salary+=item.get_salary()
        return sum_salary
class Employer:
    def __init__(self,salary):
        self.salary=salary
    def get_salary(self):
        return self.salary
class Ordinary_straff(Employer):
    def __init__(self,salary):
        super().__init__(salary)
    def get_salary(self):
        return super().get_salary()
class Programmer(Employer):
    def __init__(self,salary,commission):
        super().__init__(salary)
        self.commission=commission
    def get_salary(self):
        return super().get_salary()+self.commission
class TestControler(Employer):
    def __init__(self,salary,count):
        super().__init__(salary)
        self.count=count
    def get_salary(self):
        return super().get_salary()+self.count*5
s01=Staff_Manager()
s01.storage_staff(Ordinary_straff(2000))
s01.storage_staff(Programmer(5000,2000))
s01.storage_staff(TestControler(3000,1000))
print(s01.calculate_all_salary())