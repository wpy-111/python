"""
   练习:使用列表推式生成1---50之间,能够被3或者5整除的数字
"""
list_result= [i for i in range(1, 51) if i % 3 == 0 or i % 5 == 0]
print(list_result)
# 使用列表推式生成5---20之间数字的三次方
list02=[i**3 for i in range(5,21)]
print(list02)