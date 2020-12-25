"""
   作业:将1970到2050年之间所有润年,存入列表.
"""
list = []
for i in range(1970, 2051):
    if i % 4 == 0 and i % 100 != 0 or i % 400 == 0:
        list.append(i)
print(list)
