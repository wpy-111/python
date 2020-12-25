"""
使用selenium登录豆瓣网站  iframe子页面
"""
from selenium import webdriver
import time
#1.打开豆瓣网
browser = webdriver.Chrome()
browser.get('https://www.douban.com/')
#2.切换到iframe子页面
frame_node = browser.find_element_by_xpath('//*[@id="anony-reg-new"]/div/div[1]/iframe')
browser.switch_to.frame(frame_node)
#3.找到密码登录节点，并点击
browser.find_element_by_xpath('/html/body/div[1]/div[1]/ul[1]/li[2]').click()

#4.用户名 密码登录
browser.find_element_by_id('username').send_keys('15834383659')
browser.find_element_by_name('password').send_keys('wpy807807')
browser.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div[5]/a').click()
time.sleep(3)
browser.find_element_by_xpath('//*[@id="db-nav-sns"]/div/div/div[3]/ul/li[2]/a').click()
browser.quit()





