"""
   在终端当中循环录入字符串,如果录入空格则打印所有内容
   列表转化为字符串:
                 字符串  ="连接符".join(列表)
"""
list=[]
while True:
    str_input=input("请输入字符串:")
    if str_input == " ":
        break
    list.append(str_input)
list_result="".join(list)
print(list_result)
