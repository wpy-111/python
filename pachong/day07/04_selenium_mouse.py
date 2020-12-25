"""
 如何操作鼠标
 打开百度 鼠标移动到设置 节点 找到高级搜索并点击
"""
from selenium import webdriver
#导入鼠标事件类
from selenium.webdriver import ActionChains
#1.打开百度
browser = webdriver.Chrome()
browser.get('http://www.baidu.com/')
#2.查找设置节点，并将鼠标移动到此节点
set_node = browser.find_element_by_xpath('//*[@id="s-usersetting-top"]')
#实例化 + 指定行为 + 执行行为
ActionChains(browser).move_to_element(to_element=set_node).perform()
#3.找到高级搜索节点，并点击
browser.find_element_by_link_text('高级搜索').click()






