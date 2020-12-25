"""
   练习: 将一个列表,转化为一个字典
  人名:["张无忌","赵敏","小赵"]
"""
list=["张无忌","赵敏","小赵"]
dict={item:len(item) for item in list}
print(dict)
# 练习2 将两个列表,转化为一个字典
# 人名:["张无忌","赵敏","小赵"]
# 房间号:[101,102,103]
name=["张无忌","赵敏","小赵"]
room=[101,102,103]
for item in range(len(name)):
    dict[name[item]]=room[item]
print(dict)
# dict={name[item]:room[item] for item in range(len(name))}
# print(dict)
# 练习3 将字典的key和value交换
dict={room[item]:name[item] for item in range(len(name))}
print(dict)