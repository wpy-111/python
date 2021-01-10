"""
 豆瓣验证码
"""
from selenium import webdriver
import time
from selenium.webdriver import ActionChains
def get_tracks(distance):
    v = 0
    t = 0.3
    #0.3秒的位移
    tracks = []
    current = 0
    mid = distance * 4/5
    while current < distance:
        if current < mid:
            a = 2
        else:
            a = -3
        v0 = v
        s = v0*t + 0.5*a*(t**2)
        current += s
        tracks.append(round(s))
        v = v0 + a*t
    return tracks


options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
browser = webdriver.Chrome(options=options)
browser.get('https://www.douban.com/')
#切换到子页面
login_frame = browser.find_element_by_xpath('//*[@id="anony-reg-new"]/div/div[1]/iframe')
browser.switch_to.frame(login_frame)
#密码登录
browser.find_element_by_xpath('/html/body/div[1]/div[1]/ul[1]/li[2]').click()
time.sleep(1)
browser.find_element_by_xpath('//*[@id="username"]').send_keys('15834383659')
browser.find_element_by_xpath('//*[@id="password"]').send_keys('wpy807807')
browser.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div[5]/a').click()
time.sleep(2)
#滑块子页面

auth_frame = browser.find_element_by_xpath('/html/body/iframe')
browser.switch_to.frame(auth_frame)
time.sleep(2)
#按住
element = browser.find_element_by_xpath('//*[@id="tcaptcha_drag_button"]')
ActionChains(browser).click_and_hold(on_element=element).perform()
#move_to_element_with_offset():移动到距离某个元素（左上角的坐标）多少距离的位置
ActionChains(browser).move_to_element_with_offset(to_element=element,xoffset=180,yoffset=0).perform()
#使用加速度函数移动距离
taracks = get_tracks(26)
for track in taracks:
    #move_by_offset鼠标从当前位置移动到某个坐标
    ActionChains(browser).move_by_offset(xoffset=track,yoffset=0).perform()
time.sleep(1)
#释放鼠标
ActionChains(browser).release().perform()






