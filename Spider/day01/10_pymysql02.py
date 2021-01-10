import pymysql
db = pymysql.connect(host='localhost',
                     port = 3306,
                     user = 'root',
                     password = '123456',
                     database = 'maoyandb',
                     charset = 'utf8')
cur = db.cursor()
r_list = [("月光报盒",'周星驰','1993'),("大话西游",'周星驰','1990')]
ins = "insert into maoyantab values (%s,%s,%s)"
for i in r_list:
    cur.execute(ins,[i[0],i[1],i[2]])
db.commit()
cur.close()
db.close()