from selenium import webdriver


def element_id():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get("https://www.baidu.com")
    try:
        driver.find_element_by_id("ww")
        print("find element according to ID")
    except Exception as e:
        print("element Exception",format(e))
        #element Exception Message: Unable to locate element: [id="ww"]
    driver.quit()


element_id()