"""
   作业:定义数据结构,存储以下信息
   ---多个人多个数据
   qtx:"编码","看书","跑步"
   lzmly:"看电影","编码"
   打印qtx的所有爱好(一行一个)
   所有人的所有爱好(一行一个)
"""
dict={"qtx":["编码","看书","跑步"],
      "lzmly": ["看电影", "编码"]}
# for item in dict["qtx"]:
#     print(item)
for ixm in dict.values():
    for value in ixm:
        print(value)

