import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import requests
import datetime
cookie=os.environ['COOKIE']


def wh():
    time = datetime.datetime.now().strftime('%H:%M')
    sj = time.split(':')
    if int(sj[0]) <= 8:
        print('早上好')
    else:
        if int(sj[0]) <= 11:
            whh = '上午好'
        else:
            if int(sj[0]) <= 13:
                whh = '中午好'
            else:
                if int(sj[0]) <= 17:
                    whh = '下午好'
                else:
                    if int(sj[0]) <= 24:
                        whh = '晚上好'
    return whh


def ts(key):
    if len(key)<5:
        print(xm,'未设置token，跳过推送')
    else:
        tittle = '{}，{}同学'.format(wh(),xm)
        url = 'http://pushplus.hxtrip.com/customer/push/send?token=' + key + '&title='+ tittle+'&content='+content
        requests.get(url)

        
        
def dk(user,pas,key):
    global content
    global xm
