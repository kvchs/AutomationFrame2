from selenium import webdriver


def element_id():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get("https://www.baidu.com")
    try:
        driver.find_element_by_class_name('s_ipt')
        print("find element according to class name")
    except Exception as e:
        print("element locator Exception",format(e))
    driver.quit()


element_id()