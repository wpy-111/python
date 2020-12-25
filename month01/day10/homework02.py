"""
   作业：创建敌人类
   -----数据：名称，血量，攻击力，防御力
   -----行为：打印个人信息
   -----创建敌人列表
   -----在敌人列表中查找“灭霸”对象
   -----在敌人列表中查找死人
   -----在敌人列表中查找攻击力最大的敌人
   -----根据防御力，对敌人列表进行降序排列
"""
class Enemy:
    def __init__(self,name,blood_volume,aggressivity,defense):
        self.name=name
        self.blood_volume=blood_volume
        self.aggressivity=aggressivity
        self.defense=defense
    def print_personal_info(self):
        print("名称%s,血量：%d,攻击力：%f,防御力：%f"%(self.name,self.blood_volume,self.aggressivity,self.defense))
list_enemy=[Enemy("赵云",1000,100,100),
            Enemy("韩信",800,200,80),
            Enemy("死神",0,200,80),
            Enemy("马克波罗",800,300,50),
            Enemy("灭霸",2000,100,100),
            Enemy("死灰",0,100,100)
]
# -----在敌人列表中查找“灭霸”对象
def find_meiba():
    for item in list_enemy:
        if item.name=="灭霸":
            return item
re=find_meiba()
if re:
    re.print_personal_info()
# -----在敌人列表中查找死人
print("---------")
def find_dead():
    list_dead=[]
    for item in list_enemy:
        if item.blood_volume==0:
            list_dead.append(item)
    return list_dead
for item in find_dead():
    item.print_personal_info()
# -----在敌人列表中查找攻击力最大的敌人
print("---------")
def find_attack_most_big():
    attack_most_big= list_enemy[0]
    for item in range(1,len(list_enemy)):
        if attack_most_big.aggressivity <list_enemy[item].aggressivity:
            attack_most_big=list_enemy[item]
    return attack_most_big
find_attack_most_big().print_personal_info()
# -----根据防御力，对敌人列表进行降序排列
print("---------")
def descending_order():
    for c in range(len(list_enemy)-1):
        for i in range(c,len(list_enemy)):
            if list_enemy[c].defense<list_enemy[i].defense:
                list_enemy[c],list_enemy[i]=list_enemy[i],list_enemy[c]
descending_order()
for item in list_enemy:
    item.print_personal_info()