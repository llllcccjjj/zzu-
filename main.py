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
    try:
        content = '自动打卡失败，请您手动打卡'
        # 模拟浏览器打开网站
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        driver = webdriver.Chrome('/usr/bin/chromedriver', chrome_options=chrome_options)
        driver.get("https://jksb.v.zzu.edu.cn/vls6sss/zzujksb.dll/first0")
        driver.implicitly_wait(15)
        driver.find_element_by_name('uid').send_keys(user)
        driver.find_element_by_name('upw').send_keys(pas)
        driver.find_element_by_name('smbtn').click()
        driver.implicitly_wait(15)
        driver.get(driver.find_element_by_id('zzj_top_6s').get_attribute('src'))
        xm=driver.find_element_by_xpath('//*[@id="bak_0"]/div[13]/div[3]/span[3]').text
        driver.find_element_by_xpath('//span[text()="本人填报"]').click()
        driver.implicitly_wait(15)
        driver.find_element_by_xpath('//span[text()="提交表格"]').click()
        content = '今日打卡成功，祝您生活愉快'
        print(xm,"今日打卡成功")
    except:
        ts(key)
    else:
        ts(key)

if __name__ == "__main__":
    b = cookie.split('\n')
    for i in range(len(b)):
        sum = b[i].count(';')
        
        if sum == 1:# 补充token
            dd = b[i] + ';None'
            b[i] = dd
        c = b[i].split(';')  # 针对每组b拆分
        for m in range(len(c)):  # 拆分C，并赋值给name，pwd，token
            if m == 0:
                name = c[m]
                print('name=', name, end="  ")
            if m == 1:
                pwd = c[m]
                print('pwd=', pwd, end='  ')
            if m == 2:
                token = c[m]
                print('token=', token)
                dk(name,pwd,token)
