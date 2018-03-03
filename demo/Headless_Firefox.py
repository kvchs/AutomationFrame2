from selenium import webdriver

options = webdriver.FirefoxOptions()
options.set_headless()
# options.add_argument(‘-headless‘)
options.add_argument('--disable-gpu')
driver=webdriver.Firefox(firefox_options=options)
driver.get('http://httpbin.org/user-agent')
driver.get_screenshot_as_file('test.png')
driver.close()


# 实例化FirefoxOptions
#
# 用set_headless
#
# 或add_headless
#
# 实例化firefox浏览器的时候，增加参数firefox_options=options
#
# 这样就可以了。
#
# ‘--disable-gpu‘这句是禁用GPU加速。


# from selenium.webdriver import Firefox
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.firefox.options import Options
# from selenium.webdriver.support import expected_conditions as expected
# from selenium.webdriver.support.wait import WebDriverWait
#
# if __name__ == "__main__":
#     options = Options()
#     options.add_argument('-headless')  # 无头参数
#     driver = Firefox(firefox_options=options)  # 配了环境变量第一个参数就可以省了，不然传绝对路径
#     wait = WebDriverWait(driver, timeout=10)
#     driver.get('http://www.google.com')
#     wait.until(expected.visibility_of_element_located((By.NAME, 'q'))).send_keys('headless firefox' + Keys.ENTER)
#     wait.until(expected.visibility_of_element_located((By.CSS_SELECTOR, '#ires a'))).click()
#     print(driver.page_source)
#     driver.quit()