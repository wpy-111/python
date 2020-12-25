"""
  抓取数据  非结构化数据的抓取
"""
import requests
import os
directory = '/home/tarena/baidu/zhaoliyin/'
if not os.path.exists(directory):
    os.makedirs(directory)
    print('ok')#所有路径全部创建
    # os.mkdir(directory)#只创建最后一个目录
url = "https://timgsa.baidu.com/timg?image&amp;quality=80&amp;size=b9999_10000&amp;sec=1605018042184&amp;di=f936f683ba5a34bf03f2fa52041976da&amp;imgtype=0&amp;src=http%3A%2F%2Fb-ssl.duitang.com%2Fuploads%2Fitem%2F201307%2F17%2F20130717175433_kVn2B.jpeg"
headers = {'User-Agent':"Win7:Mozilla/5.0 "
                      "(Windows NT 6.1; WOW64) AppleWebKit/535.1"
                      " (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1"}
html = requests.get(url,headers).content
filename = directory + url[-10:]
with open(filename,'wb')as f:
    f.write(html)
print('ok')