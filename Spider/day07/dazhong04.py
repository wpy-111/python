"""
    爬取大众点评
"""
from queue import Queue
from threading import Thread,Lock
import time
import json
import requests
from fake_useragent import UserAgent
from selenium import webdriver
class DaZhongSpider:
    #cookie也会过期
    def __init__(self):
        self.url = 'https://account.dianping.com/account/ajax/passwordLogin'
        self.headers = {'User-Agent': UserAgent().random}
        self.data = {'countrycode': '86',
'username': '15834383659',
'keepLogin': 'on',
'encryptPassword': 'SO86t/0M3XiuPC5rZrIubXWNEEgrFCZWCqMhu2QvPAvVCJ/BhdGjiMGlIGBgea9KfPFJI4378OmotjHIxEWnj+hXUyALTqupt8nYgyTDk+ivsEFZBwHvAtgD02bSxHjxLI1BZ4/HpAgq6FWkCqskHX0ihCraTzPHCDYgZRj9b84=',
'_token': 'eJyNk2tvokAUhv8LSfulRAeYYcDEbPCC2nJTQbHdZsNNSwWhiNfN/vcdWJnufmk2IeE5lznvOWfgJ1NMQqbDcAAAKDMsc4yKymyBlkiscs90OBGIkixIIoISZpngb5/MCYLAMn6xGDCdF14GrIDRa+WYEfuFQ4LISiJ8ZW/IE+QhW70Yf0JSmLeyzPeddtsLguywK1th7O3yeLdpBVnaONvxuvDSSMs28e5b4CWJ7wXb7tDbX2rXjzr6owmA+1McRt21l+yj+7zIyizIku4fnfsiCuOiNu4E5Y5XyXM6nf5RJS4y+Zd9JXUn/1mLjJra1agyx3IiR2p/At8AbAA1IN2AAxwlREluiGtOcjygJDYk0CikhBpRcomUiBqqrp/DJA/hmipf9RFwEukAoZrIWQRrEggJNUFKRJfHX5JEqVaTECVSReCqZW3rZX0v2IlhOTaJrSlFlEJKASWfkncjUs2rqwEWsD3Htk2Drp8m31qkNs9JLMKsUu+g6g99pmKyMQGwqjnT61VCVoCAnVuKUWmVlValqZNfiMT38WZHKHo8qacgEadAURSz516eo8ETTBP4MFCWw+enCeSXBzVNV3ySjoZ+Btrr9vvVsUNTxddZvlccq1+aPj707cTSpJUvXrE6i7VCn30I2XYoFtdN5r1fsG5d+1b4tg2Gub93URn7/MMGHPelzk/DtnpaSitTmbvoWFowkfu2CwbcJfSjt9nB3fp4iso2dj3HTh8DZcxPLXc5nuK1uUskqGHb6wujRSC4a0eTVRhsc6OXGka+1a3zcWMoUrbA2VJ61+T5uQfGog2xDp68xxVYDc6j97HtrJLpXH/wwHqkFbliLByofoimfx4jbeiMgi7z6zcqBDqW'}
        #创建session对象
        self.s = requests.session()

    def get_html(self):
        self.s.get()


if __name__ == '__main__':
    spider = DaZhongSpider()
    spider.get_html()