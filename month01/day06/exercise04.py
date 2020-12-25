"""
    练习:ABCACDECAB
        输出:  A:3
              B:2
"""
str_world=input("请输入字符串:")
dict={}
for item in str_world:
    if item not in dict:
        dict[item]=1
    else:
        dict[item]+=1
print(dict)
# for key,value in dict.items():
#     print("%s:%d"%(key,value))

