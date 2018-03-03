from selenium import webdriver


def element_id():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.implicitly_wait(5)
    driver.get("https://www.baidu.com")
    try:
        driver.find_element_by_tag_name("form")
        print("find element according to tag name")
    except Exception as e:
        print("Exception",format(e))

    driver.quit()


element_id()