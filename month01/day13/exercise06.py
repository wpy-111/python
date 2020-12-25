"""
    创建手雷类，定义爆炸方法
    当爆炸时，有可能伤害敌人，玩家....
    需求变化：
         房子，树，鸭子
"""
class Grenades:
    def __init__(self, atk=0):
        self.atk=atk
    def explode(self,target):
        print("爆炸")
        target.injured(self.atk)
class Object:
    def injured(self,value):
        pass
class Player(Object):
    def injured(self, value):
       print("玩家受伤")
class Enemy(Object):
    def injured(self,value):
        print("掉落装备")
class House(Object):
    def injured(self,value):
        print("房屋倒塌")
class Tree(Object):
    def injured(self,value):
        print("树倒下")
class Duck(Object):
    def injured(self,value):
        print("鸭子瞎蹦")
o01=Grenades(10)
d01=Duck()
o01.explode(d01)

