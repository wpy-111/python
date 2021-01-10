import requests
session = requests.session()
post_url = 'https://accounts.douban.com/j/mobile/login/basic'
post_data = { 'ck':'', 'name': '15834383659', 'password': 'wpy807807', 'remember': 'false', 'ticket': '', }
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36'}
x=session.post(url=post_url,data=post_data,headers=headers)
print(x)
url = 'https://www.douban.com/people/227501211/'
html = session.get(url=url,headers=headers).text
print(html)

















































































