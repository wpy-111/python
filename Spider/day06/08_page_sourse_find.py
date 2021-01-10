"""
     find()方法的应用场景

"""
from selenium import webdriver
#1.打开浏览器
browser = webdriver.Chrome()
#2.输入地址
browser.get("http://www.baidu.com")
#3.page_sourse html的结构源码
html = browser.page_source
#4.find()方法使用 从html查找字符串  不存在返回 -1   如果存在返回 非0值
#     经常用于判断是否为最后一页
browser.page_source.find('xxxxx')













