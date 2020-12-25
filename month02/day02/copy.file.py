"""
   写一个程序，实现对一个文件的拷贝
   *input()输入一个文件的位置
   *将该文件‘拷贝’到主目录下
   *文件可能是文本文件也可能是二进制文件
   *文件可能性比较大，不允许一次性读取
   温馨提示：从源文件中读取内容，写入到目标新文件中
"""
file_name=input("文件名：")
file=open(file_name,'wb')
location=input("请输入文件位置：")
try:
    with open(location,'rb') as f:
        for line in f:
            file.write(line)
except Exception as e:
    print(e)

file.close()




