"""
   作业：玩家（攻击力）攻击敌人，敌人受伤（血量）后（掉血，头顶爆头），还可能死亡（掉下装备）
        敌人（攻击力）攻击玩家，玩家受伤（血量）后（掉血，黑屏），还可能死亡（冲钱）
"""
class Player:
    def __init__(self, atk=0, hp=0):
        self.atk=atk
        self.hp=hp
    def attack(self,enemy):
        print("发起进攻")
        enemy.injured(self.atk)
    def injured(self, value):
        print("受伤了","黑屏")
        self.hp -= value
        if self.hp == 0:
            print("冲钱")
class Enemy:
    def __init__(self, atk=0, hp=0):
        self.atk=atk
        self.hp=hp
    def attack(self,player):
        print("进攻")
        player.injured(self.atk)
    def injured(self,value):
        self.hp-=value
        print("敌人掉血")
        if self.hp==0:
           print("掉落装备")
P01=Player(10,20)
E01=Enemy(10,20)
P01.attack(E01)
E01.attack(P01)
P01.attack(E01)
E01.attack(P01)