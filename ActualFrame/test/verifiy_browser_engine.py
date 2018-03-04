import time
from utils.browser_engine import BrowserEngine


class TestBrowserEngine(object):

    def open_browser(self):
        browser_engine = BrowserEngine()
        driver = browser_engine.get_browser()


test = TestBrowserEngine()
test.open_browser()