"""
   json的dump()方法
   2.1) 第1个参数: python类型的数据(字典，列表等)
   2.2) 第2个参数: 文件对象
   2.3) 第3个参数: ensure_ascii=False 序列化时编码
"""
import json
item = {'name':'地京城','price':'五百万','adress':'北京'}
with open('lianjia.json','w') as f:
    json.dump(item,f,ensure_ascii=False)