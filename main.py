# -*- coding:UTF-8 -*-
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import requests
import datetime
cookie=os.environ['COOKIE']


def wh():
    time = datetime.datetime.now().strftime('%H:%M')
    sj = time.split(':')
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
        tittle = '{}，{}同学，今日打卡☑'.format(wh(),xm)
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
        d = driver.find_element_by_xpath('//*[@id="myvs_13b"]').get_attribute('value')
        zidian = {'4101': '郑州市', '4102': '开封市', '4103': '洛阳市', '4104': '平顶山市', '4105': '安阳市', '4106': '鹤壁市',
                  '4107': '新乡市', '4108': '焦作市', '4109': '濮阳市', '4110': '许昌市', '4111': '漯河市', '4112': '三门峡市',
                  '4113': '南阳市', '4114': '商丘市', '4115': '信阳市', '4116': '周口市', '4117': '驻马店市', '4118': '济源市'}
        driver.find_element_by_xpath('//span[text()="提交表格"]').click()
        print(name,"今日打卡成功")
        ctq()
 
    except:
        driver.quit()
        ts(key)
    else:
        driver.quit()
        ts(key)
        
def ctq():
    global content
    try:
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        drive = webdriver.Chrome('/usr/bin/chromedriver', chrome_options=chrome_options)
        drive.get('http://tianqi.2345.com/')
        drive.implicitly_wait(20)
        drive.find_element_by_id('js_searchInput').click()
        drive.find_element_by_id('js_searchInput').send_keys(zidian[d].decode('utf-8').encode('gb2312'))
        drive.find_element_by_id('js_searchBtn').click()
        drive.implicitly_wait(20)
        wz = drive.find_element_by_xpath('/html/body/div[8]/div/div[1]/div[1]/em').text
        vb = drive.find_element_by_xpath('/html/body/div[9]/div[2]/div[1]/div[1]/div[2]/ul/li[1]/a[1]').text
        vn = drive.find_element_by_xpath('/html/body/div[8]/div/div[1]/div[3]/ul/li[1]/a/em').text
        uu = vb.split('\n')
        jj = vn.split('~')
        print(wz,vb,vn)
        content = zidian[d] + '今日天气:' + '\n' + uu[2] + '\n' + uu[3] + '' + uu[4] + '\n' + '最低温度' + jj[
            0] + '°C' + '\n' + '最高温度' + jj[1] + 'C' + '\n' + '祝您生活愉快~'
    except:
        content = '天气获取异常，暂不推送'
        print (zidian[d])


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
