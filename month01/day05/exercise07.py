"""
 练习 将英文语句根据单词反转
 How old are you
   字符串转化为列表:
                 列表  = 字符串.split(分离符)
"""
list= "How old are you".split(" ")
list_result = list[::-1]
result=" ".join(list_result)
print(result)