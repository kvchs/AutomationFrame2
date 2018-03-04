# from selenium import webdriver
#
#
# class BrowserEngine(object):
#     def __init__(self,driver):
#         self.driver = driver
#
#     browser_type = "Ie"
#
#     def get_browser(self):
#         if self.browser_type == "Ie":
#             driver = webdriver.Ie()
#
#         elif self.browser_type == "Chrome":
#             driver = webdriver.Chrome()
#
#         elif self.browser_type == "Firefox":
#             driver = webdriver.Firefox()
#         else:
#             driver = webdriver.Chrome()
#
#         driver.maximize_window()
#         driver.implicitly_wait(5)
#         return driver


from selenium import webdriver


class BrowserEngine(object):

    browser_type = "Firefox"

    def get_browser(self):
        if self.browser_type == "Ie":
            driver = webdriver.Ie()

        elif self.browser_type == "Chrome":
            driver = webdriver.Chrome()

        elif self.browser_type == "Firefox":
            driver = webdriver.Firefox()
        else:
            driver = webdriver.Chrome()

        driver.maximize_window()
        driver.implicitly_wait(5)
        return driver