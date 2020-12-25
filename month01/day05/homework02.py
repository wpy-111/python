"""
   作业    彩票
   双色球
   红色:6个(1-33)  不能重复
   蓝色:1个
   ----随机产生一柱彩票(列表)

"""
list=[]
while len(list)<6:
    import random
    number=random.randint(1,34)
    if number not in list:
        list.append(number)
print(list)
