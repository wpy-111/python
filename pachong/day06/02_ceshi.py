import requests
from fake_useragent import UserAgent
url = 'https://careers.tencent.com/tencentcareer/api/post/Query?timestamp=1606564895725&countryId=&cityId=&bgIds=&productId=&categoryId=&parentCategoryId=&attrId=&keyword=python&pageIndex=1&pageSize=10&language=zh-cn&area=cn'
headers = {'User-Agent':UserAgent().random}
html = requests.get(url=url,headers=headers).json()
count = int(html['Data']['Count'])
total = count//10 if count%10==0 else count//10+1
print(html)
print(count)
print(total)