"""
    爬取大众点评
"""

from selenium import webdriver
import time
class DaZhongSpider:
    def __init__(self):
        self.browser = webdriver.Chrome()
        self.url = 'https://www.dianping.com/shanghai/ch10'
    def get_html(self):
        self.browser.get(self.url)
        #关闭广告
        self.browser.find_element_by_xpath('//*[@id="J-img-pop"]/span').click()
        #点击登录
        self.browser.find_element_by_xpath('//*[@id="top-nav"]/div[1]/div[2]/span[1]/a[1]').click()
        time.sleep(2)
        #进入frame
        node = self.browser.find_element_by_xpath('//*[@id="J_login_container"]/div/iframe')
        self.browser.switch_to.frame(node)
        #点击账号登陆
        self.browser.find_element_by_xpath('/html/body/div/div[2]/div[5]/span').click()
        time.sleep(1)
        #点击手机密码登录/html/body/div/div[2]/div[5]/span
        self.browser.find_element_by_xpath('//*[@id="tab-account"]').click()
        time.sleep(1)
        self.browser.find_element_by_id('account-textbox').send_keys('15834383659')
        self.browser.find_element_by_id('password-textbox').send_keys('wpy807807')
        time.sleep(1)
        self.browser.find_element_by_xpath('//*[@id="login-button-account"]').click()



if __name__ == '__main__':
    spider = DaZhongSpider()
    spider.get_html()




























