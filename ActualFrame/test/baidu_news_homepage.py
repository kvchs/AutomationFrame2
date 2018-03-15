from utils.basepage import BasePage


class NewsHomePage(BasePage):
    sports_link = "xpath=>//*[@id='channel-all']/div/ul/li[8]/a"

    def click_sport(self):
        self.click(self.sports_link)
        self.sleep(3)