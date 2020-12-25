"""
    无界面模式设置
"""
from selenium import  webdriver
#设置无界面模式   创建功能对象
options = webdriver.ChromeOptions()
options.add_argument('--headless')
browser = webdriver.Chrome(options=options)
#打开百度
browser.get('http://www.baidu.com/')
browser.save_screenshot('baidu.png')
#关闭浏览器
browser.quit()









