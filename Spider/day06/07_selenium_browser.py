"""
   打开浏览器  ——输入百度地址 -搜索框中输入关键字
"""
from selenium import webdriver
#1.打开浏览器
browser = webdriver.Chrome()
#2.输入地址
browser.get("http://www.baidu.com")
#3.搜索关键字
browser.find_element_by_xpath('//*[@id="kw"]').send_keys('王者荣耀')
#4.点击百度一下
browser.find_element_by_xpath('//*[@id="su"]').click()
















