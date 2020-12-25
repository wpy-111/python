"""
   练习：使用面向对象的思想，描述下列情景
      防守者攻击敌人，敌人受伤，敌人还会死亡
"""
class Defender:
    def __init__(self, atk=0):
        self.atk=atk
    def attack(self,enemy):
        print("打你")
        enemy.injured(self.atk)
class Enemy:
    def __init__(self, hp=0):
        self.hp=hp
    def injured(self,atk):
        print("受伤了")
        self.hp -= atk
        if self.hp<=0:
            print("敌人死亡")

D01=Defender(100)
E01=Enemy(300)
D01.attack(E01)
print("hp",E01.hp)
D01.attack(E01)
print("hp",E01.hp)
D01.attack(E01)
print("hp",E01.hp)


