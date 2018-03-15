from utils.basepage import BasePage


class SportNewsHomePage(BasePage):
    nba_link = "xpath=>//*[@id='channel-all']/div/ul/li[13]/a"

    def lick_nba_link(self):
        self.click(self.nba_link)
        self.sleep(3)