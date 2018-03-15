# 关于基类，是这样定义的：把一些常见的页面操作的selenium封装到base_page.py这个类文件，以后每个POM中的页面类，都继承这个基类，这样每个页面类都有基类的方法
# import os
# import time
# from utils.logger import Logger
#
#
# mylog = Logger(logger="BasePage").getlog()
#
#
# class BasePage(object):
#     '''
#     把常用的selenium方法封装在这个类里面
#     '''
#     def __init__(self, driver):
#         self.driver = driver
#
#     def back(self):
#         self.driver.back()
#
#     def forward(self):
#         self.driver.forward()
#
#     def open_url(self, url):
#         self.driver.get(url)
#
#     def quit_browser(self):
#         self.driver.quit()
#
#     def get_screenshot(self):
#         # root_dir = os.path.dirname(os.path.abspath('.'))
#         # print(root_dir)
#         file_path = os.path.dirname(os.getcwd()) + "/screenshots/"
#         print(file_path)
#         rq = time.strftime("%Y%m%d%H%M%S", time.localtime(time.time()))
#         screen_name = file_path + rq + ".png"
#         try:
#             self.driver.get_screenshot_as_file(screen_name)
#             mylog.info("start save screenshot")
#         except Exception as e:
#             mylog.error("error happen", format(e))
#
#     def wait(self, seconds):
#         self.driver.implicitly_wait(seconds)
#         mylog.info("wait for %d seconds." % seconds)
#
#     # 关闭当前窗口
#     def close(self):
#         try:
#             self.driver.close()
#             mylog.info("close the window")
#         except Exception as e:
#             mylog.error("Failed to quit the window")


# ----------------------------------------------------------------------------



import time
from selenium.common.exceptions import NoSuchElementException
import os.path
from utils.logger import Logger

# create a logger instance
logger = Logger(logger="BasePage").getlog()


class BasePage(object):
    '''
    定义一个页面基类，所有页面都继承这个类，封装常用的页面操作方法在这个类里面
    '''

    def __init__(self, driver):
        self.driver = driver

    def quit_browser(self):
        self.driver.quit()

    def forward(self):
        self.driver.forward()
        logger.info("Click forward button on current page")

    def back(self):
        self.driver.back()
        logger.info("Click back button on current page")

    #隐式等待
    def wait(self, seconds):
        self.driver.implicitly_wait(seconds)
        logger.info("wait for %d seconds" % seconds)

    def close_window(self):
        try:
            self.driver.close()
            logger.info("Closing current window")
        except Exception as e:
            logger.error("No find such window, can not close it" %e)

    def get_screen_img(self):
        '''
        把屏幕截图保存到项目根目录的screenshots文件夹下
        :return:
        '''
        file_path = os.path.dirname(os.path.abspath('.')) + '/screenshots/'
        rq = time.strftime('%Y%m%d %H%M%S', time.localtime(time.time()))
        screen_name = file_path + rq + '.png'
        try:
            self.driver.get_screenshot_as_file(screen_name)
            logger.info('take a photo and save to folder')
        except Exception as e:
            logger.error("failed to save screen_shot" %e)
            # self.get_screen_img()

    def find_element(self, selector):

        element = ''
        if "=>" not in selector:
            print("selector is incorrect")
        selector_key = selector.split("=>")[0]
        selector_value = selector.split("=>")[1]
        if selector_key == 'id':
            try:
                element = self.driver.find_element_by_id(selector_value)
                logger.info("find element %s successful" % selector)
            except NoSuchElementException as e:
                logger.error("NoSuchElementException: %s" %e)
        elif selector_key == "name":
            element = self.driver.find_element_by_name(selector_value)
        elif selector_key == 'class_name':
            element = self.driver.find_element_by_class_name(selector_value)
        elif selector_key == 'link_text':
            element = self.driver.find_element_by_link_text(selector_value)
        elif selector_key == 'partial_link_text':
            element = self.driver.find_element_by_partial_link_text(selector_value)
        elif selector_key == 'tag_name':
            element = self.driver.find_element_by_tag_name(selector_value)
        elif selector_key == "xpath":
            try:
                element = self.driver.find_element_by_xpath(selector_value)
                logger.info("find element %s successful" % selector)
            except NoSuchElementException as e:
                logger.error("NoSuchElementException: %s" % e)
        elif selector_key == "css_selector":
            element = self.driver.find_element_by_css_selector(selector_value)
        else:
            raise NameError("please enter a vaild type of targeting element.")
        return  element

    # 定位元素输入
    def type(self, selector, text):

        el = self.find_element(selector)
        el.clear()
        try:
            el.send_keys(text)
            logger.info("input content %s " % text)
        except Exception as e:
            logger.error("Failed to type in input box with %s" % e)
            self.get_screen_img()

    def clear(self,selector):
        el = self.find_element(selector)
        try:
            el.clear()
            logger.info("clear text in input box successful")
        except Exception as e:
            logger.error("Failed to clear input box content" % e)
            self.get_screen_img()

    def click(self, selector):
        el = self.find_element(selector)
        try:
            el.click()
            logger.info("the element is clicked")
        except Exception as e:
            logger.error("Failed to click the element")

    def get_page_title(self):
        logger.info("Current page title is %s" % self.driver.title)
        return self.driver.title

    @staticmethod
    def sleep(seconds):
        time.sleep(seconds)
        logger.info("sleep for %d seconds" %seconds)




