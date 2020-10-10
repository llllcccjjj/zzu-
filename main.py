from selenium import webdriver
import sys

def dk(user,pas):
    try:
        option = webdriver.ChromeOptions()
        option.add_argument('--headless')
        option.add_argument('--no-sandbox')
        driver = webdriver.Chrome()
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
