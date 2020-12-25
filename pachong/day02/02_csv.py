"""
     csv模块使用

"""
import csv
with open("风云.csv",'w') as f:
    #1.初始化写入对象
    #2.写入数据
    writer = csv.writer(f)
    writer.writerow(["别风",'血刀'])
