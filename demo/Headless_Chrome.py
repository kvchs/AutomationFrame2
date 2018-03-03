from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.get("https://cnblogs.com/")
driver.get_screenshot_as_file('test.png')
doc = driver.page_source
print(doc)


# from selenium import webdriver
# options=webdriver.ChromeOptions()
# options.set_headless()
# # options.add_argument(‘--headless‘)
# options.add_argument('--disable-gpu')
# driver=webdriver.Chrome(options=options)
# driver.get('http://httpbin.org/user-agent')
# driver.get_screenshot_as_file('test.png')
# driver.close()

# 实例化ChromeOptions
#
# 用set_headless
#
# 或add_headless
#
# 实例化firefox浏览器的时候，增加参数chrome_options=options
#
# 这样就可以了。
#
# ‘--disable-gpu‘这句是禁用GPU加速。