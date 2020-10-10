from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

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
        driver.find_element_by_xpath('//*[@id="bak_0"]/div[13]/div[3]/div[4]').click()
        driver.implicitly_wait(10)
        driver.find_element_by_xpath('//span[text()="提交表格"]').click()
        print("1111111111111")
    except:
        driver.quit()
        print("执行失败!")
    else:
        driver.quit()
        print("success")


if __name__ == "__main__":
    dk('201677H0323', '08286050')
