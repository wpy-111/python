"""
    挑选所有大于10的整数
"""
list01=[11,2,"a",True,33]
def get_more_than10_int(target):
    for item in target:
        if type(item)==int and item >10:
            yield item
# for item in get_more_than10_int(list01):
#     print(item)
for item in (item for item in list01 if isinstance(item,int) and item >10):
    print(item)
