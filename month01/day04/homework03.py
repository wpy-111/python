"""
   在终端中,循环录入你的喜欢de 零食,如果空字符串,则打印:
     所有零食(一行一个)
     前三个
     总数
"""
# list=[]
# while True:
#     snack =input("请输入你喜欢的零食:")
#     if snack == " ":
#         for message in list:
#             print(message)
#     else:
#         list.append(snack)
list_name=[]
while True:
    name = input("请输入你喜欢打人:")
    if name == " ":
        break
    else:
        list_name.append(name)
# for i in list_name:
#     print(i)
print(len(list_name))


