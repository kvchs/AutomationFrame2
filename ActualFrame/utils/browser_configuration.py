# 需要解决drivers 文件路径调用问题
import configparser
import os.path
from selenium import webdriver
from utils.logger import Logger

logger = Logger(logger="BrowserConfiguration").getlog()

class BrowserConfiguration(object):
    # dir = os.path.dirname(os.path.abspath('.'))
    dir = os.path.dirname(os.getcwd())
    print(dir)
    driver_path_chrome = dir + "/drivers/chromedriver.exe"
    driver_path_firefox = dir + "/drivers/geckodriver.exe"
    driver_path_ie = dir + "/drivers/IEDriverServer.exe"

    # __init__里面的构造函数，意思就是创建一个对象就会自动有一个driver变量；在实际脚本过程中unittest中的setUp方法里，browser=BrowserEngine(self)，只是创建了一个BrowserEngine对象而已，对象一创建，就掉构造函数，就有driver这个属性，接下来语句self.driver = browser.get_browser(),就告诉了driver是哪一个具体的浏览器实例
    def __init__(self, driver):
        self.driver = driver

    # read the browser type from config.ini file, return the driver
    # def open_browser(self, driver):
    def open_browser(self, driver):
        config = configparser.ConfigParser()
        file_path = os.path.dirname(os.getcwd()) + "/config/config.ini"
        print(file_path)
        # grader_father = os.path.abspath(os.path.dirname(os.getcwd()) + os.path.sep + "..")
        # grader_father = os.path.abspath(os.path.dirname(os.getcwd()))
        # print(grader_father)
        config.read(file_path, "utf-8")

        browser = config.get("browserType", "browserName")
        logger.info("you selected %s browser." %browser)
        url = config.get("testURL", "URL")
        logger.info("The test URL is: %s" %url)

        if browser == "Firefox":
            driver  = webdriver.Firefox(self.driver_path_firefox)
            logger.info("Starting open firefox browser")
        elif browser == "Chrome":
            driver = webdriver.Chrome(self.driver_path_chrome)
            logger.info("Starting Chrome browser")
        elif browser == "Ie":
            driver  = webdriver.Ie(self.driver_path_ie)
            logger.info("Starting open firefox Ie")

        driver.maximize_window()
        logger.info("Maximize the current window")
        driver.get(url)
        logger.info("Open url: %s" %url)
        driver.implicitly_wait(5)
        logger.info("implicitly 5 seconds")
        return driver

    def quit_browser(self):
        logger.info("Close and quit the browser")
        self.driver.quit()


