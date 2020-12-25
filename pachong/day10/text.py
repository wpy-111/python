import requests
from lxml import etree
def get_result():
    url = 'http://www.1ppt.com/xiazai/'
    headers={'User-Agent':"Win7:Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1",
            'Cookie': 'acw_tc=276082a616081233689254553e8a4997a1c4c255d8d26c3f330bd335c07c6b; UM_distinctid=1766b9f4d4623-0957118006a807-594a2011-144000-1766b9f4d473e8; CNZZDATA5092133=cnzz_eid%3D1524465396-1608119640-%26ntime%3D1608119640; acw_sc__v2=5fda03ef15738ccf788346ea2b6d5b000ff17d1c'
             }
    html = requests.get(url=url,headers =headers).text
    p = etree.HTML(html)
    # 2.基准的xpath，得到十个dd节点对象的列表
    dd_list = p.xpath('//div[@class="col_nav clearfix"]/ul/li/a/text()')
    print(dd_list)