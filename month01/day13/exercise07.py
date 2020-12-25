"""
   定义：
     1.存储所有图形
     2.计算所有图形的面积he
"""
class GraphicManager:
    def __init__(self):
        self.__list_graphic=[]
    def add_figure(self, target):
        self.__list_graphic.append(target)
    def totally_area(self):
        sum_area=0
        for item in self.__list_graphic:
            sum_area=item.calculate_area()
        return sum_area
class Figures:
    def calculate_area(self):
        pass
class Rond(Figures):
    def __init__(self,r):
        self.r=r
    def calculate_area(self):
        return 3.14*self.r**2
class Rectangle(Figures):
    def __init__(self,c,i):
        self.c=c
        self.i=i
    def figure_area(self):
        return  self.c*self.i
g01=GraphicManager()
g01.add_figure(Rectangle(3,5))
g01.add_figure(Rectangle(5,8))
g01.add_figure(Rond(5))
g01.add_figure(Rond(9))
g01.totally_area()
print(g01.totally_area())