"""
   定义 my——zip实现下列效果
   for item in my——zip
"""
list01=[101,102,103]
list02=["孙悟空","八戒","唐僧","武警"]
def my_zip(iterable01, iterable02):
    if len(iterable02)< len(iterable01):
        for i in range(len(iterable02)):
            yield (iterable01[i], iterable02[i])
    else:
        for i in range(len(iterable01)):
            yield (iterable01[i], iterable02[i])
for item in my_zip(list01,list02):
    print(item)
