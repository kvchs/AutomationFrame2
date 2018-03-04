import time
from selenium import webdriver
from utils.logger import Logger


mylogger = Logger(logger="MyTestLog").getlog()


class MyTestLog(object):

    def print_log(self):
        driver = webdriver.Chrome()
        mylogger.info("open browser")
        driver.maximize_window()
        mylogger.info("max window")
        driver.implicitly_wait(5)
        driver.get("https://www.baidu.com")
        mylogger.info("open baidu home page")
        time.sleep(2)
        mylogger.info("wait one s")
        driver.quit()
        mylogger.info("quit browser")


testlog = MyTestLog()
testlog.print_log()
