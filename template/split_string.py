import time
from selenium import webdriver


class GetSubString(object):

    def get_search_result(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(2)

        driver.get("https://www.baidu.com")
        driver.find_element_by_xpath("//*[@id='kw']").send_keys("selenium")
        driver.find_element_by_id("su").click()
        time.sleep(1)
        search_result_string = driver.find_element_by_xpath("//div[@class='nums']").text
        print(search_result_string)

        new_string = search_result_string.split('约')[1]
        print(new_string)
        last_string = new_string.split('个')[0]
        print(last_string)


getstring = GetSubString()
getstring.get_search_result()