import os
import time
from utils.logger import Logger


mylog = Logger(logger="BasePage").getlog()

class BasePage(object):
    '''
    把常用的selenium方法封装在这个类里面
    '''
    def __init__(self, driver):
        self.driver = driver

    def back(self):
        self.driver.back()

    def forward(self):
        self.driver.forward()

    def open_url(self, url):
        self.driver.get(url)

    def quit_browser(self):
        self.driver.quit()

    def get_screenshot(self):
        # root_dir = os.path.dirname(os.path.abspath('.'))
        # print(root_dir)
        file_path = os.path.dirname(os.getcwd()) + "/screenshots/"
        print(file_path)
        rq = time.strftime("%Y%m%d%H%M%S", time.localtime(time.time()))
        screen_name = file_path + rq + ".png"
        try:
            self.driver.get_screenshot_as_file(screen_name)
            mylog.info("start save screenshot")
        except Exception as e:
            mylog.error("error happen", format(e))

