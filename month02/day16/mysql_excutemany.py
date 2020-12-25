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
list=[1,2,3]
sql="update cls set age=age+10,score=%s where id = %s"
cur.executemany(sql,[(5,1)])
bd.commit()



#关闭游标和数据库
cur.close()
bd.close()