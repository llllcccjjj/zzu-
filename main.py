import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import requests
import datetime
from selenium.webdriver.support.select import Select
import time
cookie=os.environ['COOKIE']


def wh():
    time = datetime.datetime.now().strftime('%H:%M')
    sj = time.split(':')
    whh = '早上好'
    if int(sj[0])+8 <= 8:
         whh = '早上好'
    else:
        if int(sj[0])+8 <= 11:
            whh = '上午好'
        else:
            if int(sj[0])+8 <= 13:
                whh = '中午好'
            else:
                if int(sj[0])+8 <= 17:
                    whh = '下午好'
                else:
                    if int(sj[0])+8 <= 24:
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
    global zidian
    global xm
    global content
    global d
    try:
        content = '自动打卡失败，请您手动打卡'
        # 模拟浏览器打开网站
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        driver = webdriver.Chrome()
        driver.get("https://jksb.v.zzu.edu.cn/vls6sss/zzujksb.dll/first0")
        driver.implicitly_wait(15)
        driver.find_element(xpath('//*[@id="mt_5"]/div[2]/div[3]/input')).send_keys(user)
        driver.find_element_by_name('upw').send_keys(pas)
        driver.find_element_by_name('smbtn').click()
        driver.implicitly_wait(15)
        driver.get(driver.find_element_by_id('zzj_top_6s').get_attribute('src'))
        try:
            xm=driver.find_element_by_xpath('//*[@id="bak_0"]/div[13]/div[3]/span[3]').text
        finally:
            driver.find_element_by_xpath('//span[text()="本人填报"]').click()
            driver.implicitly_wait(15)
            opt = driver.find_element_by_name('myvs_13')
            Select(opt).select_by_value('g')
            driver.find_element_by_xpath('//*[@id="bak_0"]/div[8]/div[2]/div[2]/div[2]/div[6]/div[4]').click()
            content = '今日打卡☑'
            print(name,"今日打卡成功")      
    except:
        driver.quit()
        xm = ''
        ts(key)
    else:
        driver.quit()
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

            if m == 1:
                pwd = c[m]

            if m == 2:
                token = c[m]
                
                dk(name,pwd,token)
