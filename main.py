import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import requests
token=os.environ['PLUS_KEY'] #得到push_plus的token
sum = 0
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
    except:
        driver.quit()
        print("执行失败!")
        global sum
        sum = sum +1
        title= '打卡执行情况' #改成你要的标题内容
        content = '第'+str(sum)+'个号打卡失败'#改成你要的正文内容
        url = 'http://pushplus.hxtrip.com/customer/push/send?token='+token+'&title='+title+'&content='+content
        requests.get(url)
    else:
        driver.quit()
        print("success")
        global sum
        sum = sum +1
        title= '打卡执行情况' #改成你要的标题内容
        content = '第'+str(sum)+'个号打卡成功' #改成你要的正文内容
        url = 'http://pushplus.hxtrip.com/customer/push/send?token='+token+'&title='+title+'&content='+content
        requests.get(url)

s_name = os.environ['S_NAME'] # 获取学号信息。
s_name_num = int(s_name.count('&'))+1
print("你输入了%d个学号" % s_name_num)
list1 = s_name.split("&")

s_pwd = os.environ['S_PWD']  # 获取登陆密码信息
s_pwd_num = int(s_pwd.count('&'))+1
print("你提供了%d个登陆密码" % s_pwd_num)
list2 = s_pwd.split("&")


if __name__ == "__main__":
    for i in range(s_name.count('&')+1):
        dk(list1[i],list2[i])
