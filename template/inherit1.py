from selenium import webdriver
import time


class ClassOne(object):

    def open_baidu(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://www.baidu.com")
        time.sleep(1)
        driver.quit()
