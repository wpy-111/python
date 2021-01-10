"""
    爬取有到翻译结果
         json.loads() 将json字符串转换为python数据类型
"""
import time
import random
import requests
from hashlib import md5

data={
    "i": "query",
    "from": "AUTO",
    "to": "AUTO",
    "smartresult": "dict",
    "client": "fanyideskweb",
    "salt": "16058733508675",
    "sign": "b6ca043054de2917e04e35fab3456df2",
    "lts": "1605873350867",
    "bv": "b0ff5d17f404993192085bf8b1e93587",
    "doctype": "json",
    "version": "2.1",
    "keyfrom": "fanyi.web",
    "action": "FY_BY_REALTlME"
}
class YouDao:
    def __init__(self):
        #f12抓包抓到的post地址
        self.post_url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
        self.headers = {
    "Cookie": "OUTFOX_SEARCH_USER_ID=1019468713@10.108.160.208; OUTFOX_SEARCH_USER_ID_NCOO=755310202.2146714; JSESSIONID=aaaMMs9wveeGkhmimFLxx; ___rl__test__cookies=1605873350862",
    "Referer": "http://fanyi.youdao.com/",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36",
}
    def get_salt_sign_ts(self,word):
        ts = str(int(time.time()*1000))
        salt = ts + str(random.randint(0,9))
        string = "fanyideskweb" + word + salt + "]BjuETDhU)zqSxf-=B#7m"
        s = md5()
        s.update(string.encode())
        sign = s.hexdigest()
        return salt,sign,ts

    def attack_yd(self,word):
        salt,sign,ts = self.get_salt_sign_ts(word)
        data = {    "i": word,
                    "from": "AUTO",
                    "to": "AUTO",
                    "smartresult": "dict",
                    "client": "fanyideskweb",
                    "salt": salt,
                    "sign": sign,
                    "lts": ts,
                    "bv": "b0ff5d17f404993192085bf8b1e93587",
                    "doctype": "json",
                    "version": "2.1",
                    "keyfrom": "fanyi.web",
                    "action": "FY_BY_REALTlME"
                    }
        #.json()将json字符串转换为python数据类型
        html = requests.post(url=self.post_url,headers=self.headers,data=data).json()
        # print(html) #得到的是字符串 json数据  .text
        result = html['translateResult'][0][0]['tgt']
        return result

    def run(self):
        word = input("请输入要翻译的单词:")
        result = self.attack_yd(word)
        print("翻译结果:",result)
if __name__ == '__main__':
    spoder =YouDao()
    spoder.run()




