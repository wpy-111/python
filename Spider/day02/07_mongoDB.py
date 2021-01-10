"""
  库：maoyandb
  集合：mayanset
  在mongondb中插入一条文档：{'name'：'速度与激情','time':'2000'}
"""
#sudo pip install pymongon
import pymongo
#1.连接mongon数据库
con =pymongo.MongoClient('localhost',27017)
#2.创建库对象
db = con['maoyandb']
#3.创建集合对象
myset = db['maoyanset']
#4.插入文档
myset.insert_one({'name':'速度与激情','time':'2000'})
print('ok')