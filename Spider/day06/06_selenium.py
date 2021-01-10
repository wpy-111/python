"""
    导入selenium 的 webdriver
"""
from selenium import webdriver
# 打开浏览器 ——创建浏览器对象
browser = webdriver.Chrome()
#输入地址
browser.get("http://www.baidu.com/")
#获取屏幕截图
browser.save_screenshot('baidu.png')
#关闭浏览器
browser.quit()