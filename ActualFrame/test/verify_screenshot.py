import time
from selenium import webdriver
from utils.basepage import BasePage


class TestScreenshot(object):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(5)
    basepage = BasePage(driver)

    def get_screen(self):
        self.basepage.open_url("https://www.baidu.com")
        time.sleep(2)
        self.basepage.get_screenshot()
        self.basepage.quit_browser()


test = TestScreenshot()
test.get_screen()