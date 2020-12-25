"""
   字典的函数
"""
dict01={"悟空":65,5:68,"撒谎僧":"年来"}
dict02={"和尚":85,4:12,"白龙吗":"来"}
print(dict01.get("悟空"))#查找键所对打值
print(dict01.setdefault("悟空"))#查找键所对打值
# print(dict01.popitem())#随机返回并删除一对键值对（一般是末尾）
print(dict01.values())
# dict01.clear()#清除字典全部元素
dict01.update(dict02)#追加一个字典
print(dict01)