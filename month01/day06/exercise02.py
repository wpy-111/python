"""
   练习:在终端中录入商品信息(名陈/价格),
   录入空格停止
   将所有商品打 名称和价格打印出来(一行一个)
   如果录入蓝"游戏机",则打印其价格
   要求:重复打商品,不能重复录入
"""
dict={}
while True:
    name = input("请输入商品名称:")
    if name == " ":
        break
    price = float(input("请输入商品价格"))
    if name not in dict:
         dict[name]=price
for key,value in dict.items():
    print("%s的价格是%f"%(key,value))
if "游戏机" in dict:
    print(dict["游戏机"])
print(len(dict))#键的个数






