"""
    练习： 定义函数，获取全局变量list01中所有偶数
           使用传统思想---使用容器存储所有数据
           使用生成器思想   ---- yield返回结果
"""
list01=[4,45,5,6,76,87,8]
# def get_evern_number():
#     list_evern_number=[]
#     for item in list01:
#         if item %2==0:
#             list_evern_number.append(item)
#     return list_evern_number
# for item in get_evern_number():
#     print(item)
def get_evern_number01():
    for item in list01:
        if item%2==0:
            yield item
for item in get_evern_number01():
    print(item)
