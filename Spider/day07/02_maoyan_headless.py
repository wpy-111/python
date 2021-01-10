"""
    使用selenium 和 chrome  抓取猫眼电影 无界面
"""
from selenium import webdriver
options = webdriver.ChromeOptions()
options.add_argument('--headless')
browser = webdriver.Chrome(options=options)
browser.get('https://maoyan.com/board/4')
def get_film():
    #基准的xpath匹配dd节点
    dd_list = browser.find_elements_by_xpath('//*[@id="app"]/div/div/div[1]/dl/dd')
    #text属性 获取字节点和后代节点的文本内容
    for dd in dd_list:
        item ={}
        list = dd.text.split('\n')
        item['number'] = list[0]
        item['name'] = list[1]
        item['star'] = list[2]
        item['score'] = list[3]
        print(item)
while True:
    get_film()
    #判断是否为最后一页，进行点击,找不到会抛出异常
    try:
        browser.find_element_by_link_text('下一页').click()
    except Exception as e:
        browser.quit()
        break













