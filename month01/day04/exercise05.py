"""
   在终端中录入一个字符串,打印每个字符编码
"""
# name = input("请输入字符串:")
# for message in name:
#     print(ord(message))
#    在终端在重复录入编码值,然后打印字符串,如果录入字符串为空,推出
while True:
    str_number = input("请输入编码值")
    if str_number == " ":
        break
    int_number = int(str_number)
    print(chr(int_number))



