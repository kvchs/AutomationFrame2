from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains


def element_id():
    driver = webdriver.Chrome()
    # options = Options()  # 实例化ChromeOptions
    # options.add_argument('-headless')  # 无头参数   set_headless/add_headless
    # options.add_argument('--disable-gpu')  # --disable-gpu这句是禁用GPU加速。
    # driver = webdriver.Chrome(chrome_options=options)
    driver.maximize_window()
    driver.implicitly_wait(5)
    # driver.set_window_size(320,480)
    # print(driver.get_window_size())
    # time.sleep(3)
    # driver.set_window_size(760,999)
    driver.get("http://news.baidu.com")
    try:
        # driver.find_element_by_id("kw").send_keys("clear")
        # time.sleep(2)
        # driver.refresh()    #刷新页面
        # driver.find_element_by_id("kw").clear()  #清除一个文本输入框内的文字
        # driver.back()  # 后退到上一页
        # driver.forward()  # 前进一页
        # print(driver.capabilities['version'])  # 打印浏览器version的值
        # note:firefox对应的driver插件是geckodriver.exe，打印不了版本号，应该是这个geckodriver.exe的bug
        # print(driver.current_url)   # 获取当前页面的URL
        # print(driver.title)   # title方法可以获取当前页面的标题显示的字段
        # 在浏览器里，我们按住 ctrl+ t 就可以新打开一个tab
        # driver.find_element_by_tag_name("body").send_keys(Keys.CONTROL,"t")   # 触发ctrl + t
        # for radio in driver.find_elements_by_xpath(".//input[@type='radio']"):
        #     radio.click()
        # assert "百度一下" in driver.title   #断言页面标题
        # 直接把字段写入XPath表达式，如果通过该XPath能定位到元素，说明这个错误字段已经在页面显示；
        # error_message = driver.find_element_by_xpath(
        #     "//*[@id='TANGRAM__PSP_8__error' and text()='请您填写手机/邮箱/用户名']").is_displayed()
        # 元素方法is_selected()返回是是布尔值，用来判断单选或者多选控件是否被选中，或者下拉选择菜单是否选择一个默认的option，都可以通过这个方法去判断。
        # 判断页面元素是不是被选中
        # print(driver.find_element_by_xpath("//*[@value='newstitle']").is_selected())
        # ele = driver.find_element_by_xpath("//*[@value='newstitle']")
        # print(ele.size)
        # 组合键-全选文字
        # ele = driver.find_element_by_tag_name("body")
        # ele.send_keys(Keys.CONTROL,"a")
        # 组合键-退格键删除文字
        # element.send_keys(Keys.BACKSPACE)
        # 鼠标右键   注意：ActionChains下相关方法在当前的firefox不工作，这个是一个已知的bug
        # element = driver.find_element_by_xpath(".//div[@id='lg']/img")
        # ActionChains(driver).context_click(element).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()
        # ActionChains(driver).context_click(element).send_keys("i").perform()
        # 执行JavaScript
        # driver.execute_script("window.alert('这是一个alert弹框。');")
        # 操作滚动条，让“地区” 部分可见
        # ele = driver.find_element_by_link_text("地区")
        # driver.execute_script("return arguments[0].scrollIntoView();", ele)  # 用目标元素参考去拖动
        # time.sleep(5)
        #
        # driver.execute_script("scroll(0,2400)")

        # 多窗口之间切换
        # print(driver.current_window_handle)
        # driver.find_element_by_xpath("//*[@id='pane-news']/div/ul/li[1]/strong/a").click()
        # print(driver.current_window_handle)
        # hands = driver.window_handles
        # print(hands)
        # for hand in hands:
        #     if hand != driver.current_window_handle:
        #         print("switch to second handle", hand)
        #         driver.close()
        #         driver.switch_to.window(hand)
        #         text = driver.find_element_by_xpath(".//div[@id='conTit']/h1").text
        #         print(text)
        # 处理iframe切换
        # driver.switch_to.frame("iframe1")
        # # 操作目标元素，这个目标元素在 iframe1里面，这里就是百度文本输入框输入文字
        # driver.switch_to.default_content()


        # 处理Alert弹窗 //firefox上无alert弹出
        # driver.execute_script("window.alert('alert');")
        # time.sleep(2)
        # driver.switch_to.alert.accept()  # 点击弹出里面的确定按钮
        # driver.switch_to.alert.dismiss()  # 点击弹出里面的确定按钮

        # 获取页面上的图片信息
        # for img in driver.find_elements_by_tag_name("img"):
        #     print(img.text, img.size, img.tag_name)

        # element = driver.find_elements_by_xpath("//*[@href]")
        # print(element)
        # for link in driver.find_elements_by_xpath("//*[@href]"):
        #     print(link.get_attribute("href"))


        driver.find_element_by_id("passLog").click()
        driver.get_screenshot_as_file("test.png")
        time.sleep(2)



    except Exception as e:
        print("Exception",format(e))
    driver.quit()


element_id()