"""
   作业：以万物揭对象的思想，洞察身边客观存在打事物，
         将其抽象为类，再创建对象

"""
class Object:
    cloths=["半袖","毛衣","长裤"]
    @classmethod
    def my_favourity(cls):
        print("我最喜欢的衣服是："+cls.cloths[0])
    def __init__(self, color, asd=None):
        self.color=color
        self.color=asd
    def favority_color(self):
        print("我最喜欢衣服的颜色是"+self.color)
Object.my_favourity()
w01=Object("黄色")
w01.favority_color()