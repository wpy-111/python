"""
   练习：使用面向对象的思想，描述下列情景
      小明在银行取钱
"""
class Person:
    def __init__(self, name="", money=0):
        self.name=name
        self.money=money
class Bank:
    def __init__(self, money=0):
        self.money=money
    def draw_money(self,value,person):
        self.money-=value
        person.money+=value
B01=Bank(100000)
P01=Person("小明",0)
B01.draw_money(1000,P01)
print(P01.money)
print(B01.money)