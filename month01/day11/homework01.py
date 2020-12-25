"""
    作业：创建技能类（技能名称，消耗法力（0-80），持续时间（1-60）
    限制对象打有效范围
"""
class Skill:
    def __init__(self, name="", mana=0,last_time=1):
        self.name=name
        self.mana=mana
        self.last_time=last_time
    @property
    def mana(self):
        return self.__mana
    @mana.setter
    def mana(self,value):
        if 0<=value<=80:
            self.__mana=value
        else:
            raise Exception("输入错误")

    @property
    def last_time(self):
        return self.__last_time

    @last_time.setter
    def last_time(self, value):
        if 1 <= value <= 60:
            self.__last_time = value
        else:
            raise Exception("输入错误")
w01=Skill("降龙十八张",50,10)
print(w01.mana)

