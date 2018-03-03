from selenium import webdriver


def element_id():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get("https://www.baidu.com")
    try:
        driver.find_element_by_partial_link_text("主页")
        print("find element according to ID")
    except Exception as e:
        print("element locator Exception",format(e))
    driver.quit()


element_id()