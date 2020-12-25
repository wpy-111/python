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
#读操作--》 fetch  =============注意引号
mes = input("查询的NAME:")

# sql="select * from cls ;"
# sql="select id,age from cls where name = '%s';"%mes
sql="select id,age from cls where name =%s"

cur.execute(sql,mes)

#遍历游标对象获取查询记录
print(cur.fetchall())

#关闭游标和数据库
cur.close()
bd.close()