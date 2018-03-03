from selenium import webdriver
driver = webdriver.Ie()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("http://www.baidu.com")
driver.quit()