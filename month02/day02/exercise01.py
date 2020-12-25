"""
   查单词
"""
f=open('/home/tarena/dict.txt')
while True:
    word = input('请输入单词：')
    for line in f:
        if line.split(" ")[0]>word:
            print("没有该单词")
        if word ==line.split(" ")[0]:
            print(line)
            break
    else:
        print("没有该单词")
