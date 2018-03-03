import time
from selenium import webdriver


def search_baidu():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get("http://www.baidu.com")
    driver.find_element_by_xpath("//*[@id='kw']").send_keys("selenium")
    driver.find_element_by_xpath("//*[@id='su']").click()
    time.sleep(2)
    #driver.find_element_by_xpath("//div/h3/a[contains(@href,'baidu')]/em[text()='Selenium']").is_displayed()
    #1.通过元素XPath表达式来确定该元素显示在结果列表，从而判断Selenium官网这个链接显示在结果列表。
    #2.采用了相对元素定位方法/../
    #3.selenium方法is_displayed() 来判断我们的目标元素是否在页面显示
    #driver.find_element_by_xpath("//div/h3/a[contains(@href,'baidu')]/../a/em[text()='Selenium']").is_displayed()

    selenium_text = driver.find_element_by_xpath("//div/h3/a[contains(@href,'baidu')]/../a/em[text()='selenium']").text
    print(selenium_text)
    if(selenium_text == "selenium"):
        print("verify pass")
    driver.quit()


search_baidu()
