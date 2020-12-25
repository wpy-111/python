"""
   练习
   猜拳
"""
tuple_win=(
         ("石头","剪刀"),
         ("布","石头"),
         ("剪刀","布")
)
import random
while True:
# 玩家一输入
    item_input=input("请输入:")
    tuple_rule=("石头","剪刀","布")
    number=random.randint(0,2)
    # 机器输入
    computer_input=tuple_rule[number]
    tuple_finally=(item_input,computer_input)
    if item_input==computer_input:
        print("平局")

    elif  tuple_finally in   tuple_win :
        print("获胜")
    else:
        print("失败")