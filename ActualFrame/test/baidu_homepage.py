# 页面对象中，包含元素定位和简单的操作函数，页面类主要是元素定位和页面操作写成函数，供测试类调用
from utils.basepage import BasePage


class HomePage(BasePage):
    input_box = "id=>kw"
    search_submit_btn = "xpath=>//*[@id='su']"
    news_link = "xpath=>//*[@id='u1']/a[1]"

    def type_search(self, text):
        self.type(self.input_box, text)

    def send_submit_btn(self):
        self.click(self.search_submit_btn)

    def click_news(self):
        self.click(self.news_link)
        self.sleep(3)
