import time
import unittest
from utils.browser_configuration import BrowserConfiguration


class BaiduSearchFrame(unittest.TestCase):

    def setUp(self):
        browser = BrowserConfiguration(self)
        self.driver = browser.open_browser(self)

    def tearDown(self):
        self.driver.quit()

    def test_baidu_search_frame(self):
        self.driver.find_element_by_id("kw").send_keys("selenium")
        self.driver.find_element_by_id("su").click()
        time.sleep(3)
        try:
            assert "selenium" in self.driver.title
            print("verify pass")
        except Exception as e:
            print("verify failed", format(e))



if __name__ == '__main__':
    unittest.main()