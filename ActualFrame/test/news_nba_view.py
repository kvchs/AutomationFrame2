# 进入一个新的页面，就要初始化这个页面的对象，然后才能调用这个页面相关的方法，driver这个实例对象在不同页面之间切换，这个就是POM的核心内容
import unittest
from utils.browser_configuration import BrowserConfiguration
from test.baidu_homepage import HomePage
from test.baidu_news_homepage import NewsHomePage
from test.news_sports_homepage import SportNewsHomePage


class ViewNBANews(unittest.TestCase):
    def setUp(self):
        browser = BrowserConfiguration(self)
        self.driver = browser.open_browser(self)

    def tearDown(self):
        self.driver.quit()

    def test_view_nba_views(self):
        # 初始化百度首页，并点击新闻链接
        baiduhome = HomePage(self.driver)
        baiduhome.click_news()
        # 初始化一个新闻主页，点击体育
        newshome = NewsHomePage(self.driver)
        newshome.click_sport()
        # 初始化一个体育主页，点击NBA
        sportnewhome = SportNewsHomePage(self.driver)
        sportnewhome.lick_nba_link()
        sportnewhome.get_screen_img()


if __name__ == '__main__':
    unittest.main()
