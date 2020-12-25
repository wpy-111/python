"""
   作业    彩票
   双色球
   红色:6个(1-33)  不能重复
   蓝色:1个
   ----在终端中购买一柱彩票
         "请输入第一个红色球号码"
         "号码超过范围"
         "已经存在"
"""
list_result=[ ]
while len(list_result)<6:
    number=int(input("请输入第%d个红球号码" % (len(list_result) + 1)))
    if number in list_result:
        print("号码已经存在")
    elif number<1 or  number>33:
        print("号码超过范围")
    else:
        list_result.append(number)
while len(list_result)<7:
    number = int(input("请输入第1个蓝球号码"))
    if number<1 or  number>16:
        print("号码超过范围")
    else:
        list_result.append(number)
print(list_result)