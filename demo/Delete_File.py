from selenium import webdriver


def element_id():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get("http://news.baidu.com/")
    try:
        driver.find_element_by_xpath(".//*[@id='passLog']").click()
        driver.find_element_by_xpath(".//*[@id='TANGRAM__PSP_12__userName']").clear()
        driver.find_element_by_xpath(".//*[@id='TANGRAM__PSP_12__submit']").click()
        print(driver.find_element_by_xpath(".//*[@id='TANGRAM__PSP_12__error']").text)
    except Exception as e:
        print("element locator Exception",format(e))
    driver.quit()


element_id()