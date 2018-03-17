import unittest
from utils.browser_configuration import  BrowserConfiguration
from test.baidu_homepage import HomePage


class GetPageTitle(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        driver = BrowserConfiguration(cls)
        cls.driver = driver.open_browser(cls)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_get_title(self):
        homepage = HomePage(self.driver)
        print(homepage.get_page_title())
