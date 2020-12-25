"""
   练习:在终端中录入人名,要求不能重复,如果录入空格则停止
   最后打印所有人名一行一个
"""
set01=set()
while True:
    name = input("请输入人名:")
    if name ==" ":
        break
    set01.add(name)
for i in set01:
    print(i)