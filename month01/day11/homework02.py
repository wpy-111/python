"""
    作业：以面向对象思想，描述下列情景
      张无忌 教 赵敏 九阳神功
      孙悟空 教 唐僧 七十二变
      赵敏 上班挣了 8000 元
      唐僧 上班挣了 5000 元
"""
class Person:
    def __init__(self, name=""):
        self.name=name
    def teach(self,person,value):
        print(self.name+"教"+person+value)
    def go_to_work(self,value):
        print(self.name,"上班挣了",value)
p01=Person("张无忌")
p02=Person("赵敏")
p03=Person("孙悟空")
p04=Person("唐僧")
p01.teach(p02.name,"九阳神功")
p03.teach(p04.name,"七十二变")
p03.go_to_work(8000)
p04.go_to_work(5000)