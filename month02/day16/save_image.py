import pymysql
#连接数据库  关键字传参
bd = pymysql.connect(host='localhost',
                     port=3306,
                     user= 'root',
                     password='123456',
                     database='stu',
                     charset='utf8')
# 创建游标对象(操作数据库执行sql语句获取结果的对象)
cur=bd.cursor()

#利用游标对象执行sql语句
f=open('桌面.jpg','rb')
data = f.read()
sql = "update cls set image=%s where id=1;"
cur.execute(sql,data)
#读操作--》 fetch
#写操作--》 commit rollba



#关闭游标和数据库
cur.close()
bd.close()