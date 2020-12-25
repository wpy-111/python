"""
   练习：定义函数，返回字符串中第一个不重复打字符
   输入：ABCACABEFD
   输出：E
"""
def print_fist_not_repeat(target):
    dict_repeat_info=get_dict_repeat_info(target)
    for key,value in dict_repeat_info.items():
        if value==1:
            return key
def get_dict_repeat_info(target):
    dict_repeat_info={}
    for i in target:
        if i not in dict_repeat_info:
            dict_repeat_info[i] = 1
        else:
            dict_repeat_info[i] += 1
    return dict_repeat_info


print(print_fist_not_repeat("ASDASFWSDFAAB"))
