from selenium import webdriver


def element_id():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get("https://www.baidu.com")
    try:
        driver.find_element_by_link_text("新闻")
        print("find element according to ID")
    except Exception as e:
        print("element locator Exception",format(e))
    driver.quit()


element_id()

#note:通过text()这个XPath中的函数也可以达到类似link text定位的目的  //*/div[@id='u1']/a[text()='新闻']