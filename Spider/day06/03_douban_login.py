"""
   Cookie 模拟登录豆瓣 - 获取个人主页信息
   方法一：手动登录成功，并抓取cookie
   在headers中添加Cookie
"""
from fake_useragent import UserAgent
import requests
def login():
    url = 'https://www.douban.com/people/227501211/'
    headers = {'User-Agent':UserAgent().random,
               'Cookie':'ll="118099"; bid=wC77nbff6_g; _vwo_uuid_v2=D57025B9BBD7E7FADE735BCA0EFB1AF41|aad514c200ec33b03247f6ae4fc61b83; ct=y; __utmz=30149280.1606025322.2.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __gads=ID=c10065b6297ad557-222ae9c8dcc4005e:T=1606025353:RT=1606025353:S=ALNI_MaiMMiDAb9h9KykCyZYjiGiH9DWXw; _pk_ses.100001.8cb4=*; __utma=30149280.1288159800.1605959824.1606025322.1606620097.3; __utmc=30149280; dbcl2="227501211:kaJz8Xi68qs"; ck=Xynp; ap_v=0,6.0; push_noty_num=0; push_doumail_num=0; __utmv=30149280.22750; __yadk_uid=dXCVhWih4YoKoyXoFlLWGXvRPhD84yCe; douban-profile-remind=1; __utmt=1; _pk_id.100001.8cb4=35f0bca7b9e391eb.1606620095.1.1606620991.1606620095.; __utmb=30149280.20.9.1606620991639'}
    html = requests.get(url=url,headers=headers).text
    print(html)
login()