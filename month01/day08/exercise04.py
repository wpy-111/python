"""
    定义函数，多个数值累加
"""
def number_accumulate(*arges,):
    result=0
    for i in arges:
        result+=i
    return result
re=number_accumulate(5,6,8,5)
print(re)
