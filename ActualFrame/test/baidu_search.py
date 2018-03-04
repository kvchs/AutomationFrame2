import time
from selenium import webdriver
from utils.basepage import BasePage


class BaiduSearch(object):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(5)
    basepage = BasePage(driver)

    def open_baidu(self):
        self.basepage.open_url("https://www.baidu.com")
        time.sleep(2)

    def test_search(self):
        self.driver.find_element_by_xpath("//*[@id='kw']").send_keys("selenium")
        time.sleep(1)
        self.basepage.back()
        time.sleep(2)
        self.basepage.forward()
        time.sleep(2)
        self.basepage.quit_browser()
        time.sleep(2)


baidu = BaiduSearch()
baidu.open_baidu()
baidu.test_search()
