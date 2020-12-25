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
#写操作--》 commit rollba
try:
    #插入操作
    # sql = "insert into cls values(%s,%s,%s,%s,%s)"
    # cur.execute(sql,[10,'csd',25,'m',100])
    # bd.commit()
    #修改操作
    # sql="update cls set score=100 where id=2;"
    # cur.execute(sql)
    # bd.commit()
    #删除操作
    sql="delete from cls where id=2"
    cur.execute(sql)
    bd.commit()
except Exception as e:
    print(e)
    bd.rollback()

#关闭游标和数据库
cur.close()
bd.close()