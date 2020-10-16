import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import requests
token=os.environ['PLUS_KEY']
s_name=os.environ['S_NAME']
s_pwd=os.environ['S_PWD']
token1=os.environ['PLUS_KEY1']
s_name1=os.environ['S_NAME1']
s_pwd1=os.environ['S_PWD1']
def dk(user,pas):
    try:
        # 模拟浏览器打开网站
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        driver = webdriver.Chrome('/usr/bin/chromedriver', chrome_options=chrome_options)
        driver.get("https://jksb.v.zzu.edu.cn/vls6sss/zzujksb.dll/first0")
        driver.implicitly_wait(10)
        driver.find_element_by_name('uid').send_keys(user)
        driver.find_element_by_name('upw').send_keys(pas)
        driver.find_element_by_name('smbtn').click()
        driver.implicitly_wait(10)
        driver.get(driver.find_element_by_id('zzj_top_6s').get_attribute('src'))
        driver.find_element_by_xpath('//span[text()="本人填报"]').click()
        driver.implicitly_wait(10)
        driver.find_element_by_xpath('//span[text()="提交表格"]').click()
        print("1111111111111")
    except:
        driver.quit()
        print("执行失败!")
        title= '打卡执行情况' #改成你要的标题内容
        content ='执行失败' #改成你要的正文内容
        url = 'http://pushplus.hxtrip.com/customer/push/send?token='+token+'&title='+title+'&content='+content
        requests.get(url)
    else:
        driver.quit()
        print("success")
        title= '打卡执行情况' #改成你要的标题内容
        content ='执行成功' #改成你要的正文内容
        url = 'http://pushplus.hxtrip.com/customer/push/send?token='+token+'&title='+title+'&content='+content
        requests.get(url)
def dk1(user,pas):
    try:
        # 模拟浏览器打开网站
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        driver = webdriver.Chrome('/usr/bin/chromedriver', chrome_options=chrome_options)
        driver.get("https://jksb.v.zzu.edu.cn/vls6sss/zzujksb.dll/first0")
        driver.implicitly_wait(10)
        driver.find_element_by_name('uid').send_keys(user)
        driver.find_element_by_name('upw').send_keys(pas)
        driver.find_element_by_name('smbtn').click()
        driver.implicitly_wait(10)
        driver.get(driver.find_element_by_id('zzj_top_6s').get_attribute('src'))
        driver.find_element_by_xpath('//span[text()="本人填报"]').click()
        driver.implicitly_wait(10)
        driver.find_element_by_xpath('//span[text()="提交表格"]').click()
        print("1111111111111")
    except:
        driver.quit()
        print("执行失败!")
        title= '打卡执行情况' #改成你要的标题内容
        content ='执行失败' #改成你要的正文内容
        url = 'http://pushplus.hxtrip.com/customer/push/send?token='+token1+'&title='+title+'&content='+content
        requests.get(url)
    else:
        driver.quit()
        print("success")
        title= '打卡执行情况' #改成你要的标题内容
        content ='执行成功' #改成你要的正文内容
        url = 'http://pushplus.hxtrip.com/customer/push/send?token='+token1+'&title='+title+'&content='+content
        requests.get(url)        
if __name__ == "__main__":
    dk(s_name, s_pwd)
    dk1(s_name1,s_pwd1)
