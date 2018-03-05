import time
import unittest
from selenium import webdriver


class BaiduSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        self.driver.get("https://www.baidu.com")

    def tearDown(self):
        self.driver.quit()

    def test_baidu_search(self):
        self.driver.find_element_by_xpath("//*[@id='kw']").send_keys("python")
        time.sleep(2)


if __name__ == '__main__':
    unittest.main()
