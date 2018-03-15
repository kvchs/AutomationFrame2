# 到一个页面，第一件事情是初始化这个页面的一个页面对象实例。注意，一定要带self.driver，不然会报错，这个self.driver，可以这样理解：在当前测试类里面，self.driver是来自浏览器引擎类中方法得到的，在初始化一个页面对象的时候，也把这个来自浏览器引擎类的driver给赋值给当前的页面对象，这样，才能执行页面对象或者基类里面的相关driver方法。


import time
import unittest
from utils.browser_configuration import BrowserConfiguration
from test.baidu_homepage import HomePage


class BaiDuSearch(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        browser = BrowserConfiguration(cls)
        cls.driver = browser.open_browser(cls)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_baidu_search(self):
        homepage = HomePage(self.driver)
        homepage.type_search("selenium")
        homepage.send_submit_btn()
        time.sleep(5)
        homepage.get_screen_img()
        try:
            assert "selenium" in homepage.get_page_title()
            print("Test pass")
        except Exception as e:
            print("Test failed.", format(e))

    def test_baidu_search2(self):
        homepage = HomePage(self.driver)
        homepage.type_search("python")
        homepage.send_submit_btn()
        time.sleep(5)
        homepage.get_screen_img()
        try:
            assert "selenium3" in homepage.get_page_title()
            print("Test pass")
        except Exception as e:
            print("Test failed.", format(e))


if __name__ == '__main__':
    unittest.main()