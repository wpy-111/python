import  pymysql
import re

bd = pymysql.connect(host='localhost',
                     port=3306,
                     password='123456',
                     user='root',
                     database='dict',
                     charset='utf8')
cur=bd.cursor()
f=open('dict.txt','r')
list=[]
for line in f:
    result=re.findall(r'(\S+)\s+(.*)',line)
    list.extend(result)
try:
    sql="insert into words (world,mean) values(%s,%s);"
    cur.executemany(sql,list)
    bd.commit()
except Exception as e:
    print(e)
    bd.rollback()
bd.close()
cur.close()







