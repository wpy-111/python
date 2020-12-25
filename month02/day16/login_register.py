#模拟登录和注册
import pymysql
bd = pymysql.connect(host='localhost',
                     port=3306,
                     user= 'root',
                     password='123456',
                     database='stu',
                     charset='utf8')
cur=bd.cursor()
def login(name,password):
    pass

def register():

    name = input("请输入注册名字：")
    sql = "select name from message "
    cur.execute(sql)
    data=cur.fetchall()
    for item in data:
        if item[0] == name:
            return print("用户已存在")
    password = int(input("请输入a注册密码"))
    try:
        sql1="insert into message (name,password) values(%s,%s)"
        cur.execute(sql1,[name,password])
        bd.commit()
    except:
        bd.rollback()

if __name__ == '__main__':
    register()
