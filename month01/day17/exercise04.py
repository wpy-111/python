"""
   定义 my——enumerate实现下列效果
   for index item in my——enumerate
"""
dict={"a":2,"b":8,"c":33,"s":86}
list=[2,8,6,9,1,95,988,8888,888995]
def my_enumerate(target):
    count=0
    for item in target:
        yield (count,item)
        count+=1

# for index,item in my_enumerate(dict):
#     print(index,item)
for index,item in my_enumerate(list):
    print(index,item)

