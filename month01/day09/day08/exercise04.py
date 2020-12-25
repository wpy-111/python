"""
   练习：
        质数：大于的整数，除了1和他本身以外不能再被其他数字整除
        定义函数，获取指定范围内打所有质数
        输入：2,20
        输出：[2,3,5,7,11,13,17,19]
"""
def get_prime_number(begin,end):
    list = []
    for item in range(begin,end):
        list_result=[]
        if item==2 or item ==3:
            list.append(item)
        else:
            for m in range(2,item):
                result=item % m
                list_result.append(result)
            if 0 not in list_result:
                list.append(item)
    return list
print(get_prime_number(2,50))



