import time
from selenium import webdriver


class BaiduSearch(object):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(5)

    def open_baidu(self):
        self.driver.get("https://www.baidu.com")
        time.sleep(2)

    def test_search(self):
        self.driver.find_element_by_xpath(".//*[@id='kw']").send_keys("selenium")
        time.sleep(1)
        print(self.driver.title)
        try:
            assert 'selenium' in self.driver.title
            print("pass")
        except Exception as e:
            print(e)
        self.driver.quit()


baidu = BaiduSearch()
baidu.open_baidu()
baidu.test_search()