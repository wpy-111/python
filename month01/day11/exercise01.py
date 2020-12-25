"""
   作业：创建敌人类
   -----数据：名称，血量，攻击力，防御力
                 0-1000 0-500 0-100
"""
class Enemy:
    def __init__(self,name,hp,attack,defense):
        self.name=name
        self.hp=hp
        self.attack=attack
        self.defense=defense
    @property
    def hp(self):
        return self.__hp
    @hp.setter
    def hp(self,value):
        if 0<= value <=1000:
            self.__hp=value
        else:
            raise Exception("错误数据")
    @property
    def attack(self):
        return self.attack
    @attack.setter
    def attack(self, value):
        if 0 <= value <= 500:
            self.__attack = value
        else:
            raise Exception("错误数据")
    @property
    def defense(self):
        return self.__defense
    @defense.setter
    def defense(self, value):
        if 0 <= value <= 100:
            self.__defense = value
        else:
            raise Exception("错误数据")
w01=Enemy("小王",1000,200,90)
print(w01.defense)
