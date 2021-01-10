import pymysql
# 1. 建立数据库连接(db = pymysql.connect(...))
# host ：主机地址,本地 localhost
# port ：端口号,默认3306
# user ：用户名
# password ：密码
# database ：库
# charset ：编码方式,推荐使用 utf8
db = pymysql.connect(host='localhost',
                     port = 3306,
                     user = 'root',
                     password = '123456',
                     database = 'maoyandb',
                     charset = 'utf8'
            )
# 2. 创建游标对象(cur = db.cursor())
cur = db.cursor()
# 3. 游标方法: cur.execute("insert ....")
cur.execute("insert into maoyantab values ('张国荣','春光无线','1990')")
# 4. 提交到数据库或者获取数据 : db.commit()/db.fetchall()
db.commit()
# 5. 关闭游标对象 ：cur.close()
cur.close()
# 6. 断开数据库连接 ：db.close()
db.close()