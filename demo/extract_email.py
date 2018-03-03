from selenium import webdriver
import re
# from selenium.webdriver.firefox.options import Options
from selenium.webdriver.chrome.options import Options

def extract_email():
    options = Options()           #实例化ChromeOptions
    options.add_argument('-headless')  # 无头参数   set_headless/add_headless
    options.add_argument('--disable-gpu')  #--disable-gpu这句是禁用GPU加速。
    #driver = webdriver.PhantomJS()
    #实例化firefox浏览器的时候，增加参数chrome_options=options
    driver =webdriver.Chrome(chrome_options=options)
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get("http://home.baidu.com/contact.html")
    #获取网页的源代码
    doc = driver.page_source
    print(doc)
    #利用正则表达式，找出XXX@XXX.XXX的字段
    #re模块的findall方法返回配置子字符串的列表
    emails = re.findall(r'[\w]+@[\w\.-]+',doc)
    #去除重复的email值
    #for email in list(set(emails)):
    for email in emails:
        print(email)
    driver.quit()


extract_email()