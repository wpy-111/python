"""
   在线对云打码网站j进行识别
"""
from selenium import webdriver
#python图像处理库
from yd import *
from PIL import Image
class YdmSpider:
    def __init__(self):
        """打开云打码网站，最大化"""
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('--start-maximized')
        self.browser = webdriver.Chrome(options=self.options)
        #输入云打码地址
        self.browser.get("http://www.yundama.com/")

    #获取验证码的图片
    def get_image(self):
        #1.获取主页截图
        self.browser.save_screenshot('index.png')
        #2.从大截图截取验证码的图片  ，验证码的左上角xy坐标，和右下角的坐标
        location = self.browser.find_element_by_xpath('').location
        #size属性获取节点的宽度和高度
        size = self.browser.find_element_by_xpath('').size
        #获取两个坐标：
        left_x = location['x']
        left_y = location['y']
        right_x = location['x'] + size['width']
        right_y = location['y'] - size['height']
        #截取验证码的图片 crop参数为元组
        img = Image.open('index.png').crop((left_x,left_y,right_x,right_y))
        img.save('verify.png')

    #获取在线识别的结果
    def get_code(self):
        result = get_result('verify.png')
        print(result)

    def run(self):
        self.get_image()
        self.get_code()
        self.browser.close()
if __name__ == '__main__':
    spider = YdmSpider()
    spider.run()






