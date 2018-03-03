# AutomationFrame2

# 1.打开IE浏览器可能出现的报错
Exception:<br/>
Message: Unexpected error launching Internet Explorer. Protected Mode settings are not the same for all zones. Enable Protected Mode must be set to the same value (enabled or disabled) for all zones.<br/>
解决办法：Internet选项->安全; 把Internet站点，本地Intrant,受信任站点 三个地方的安全界面都设置相同等级，例如都设置中； 再次运行代码就可以用IE打开百度了。

# 2.XPath定位技巧
text()方法 eg:  .//*[@id="u_sp"]/a[text()="新闻"]<br/>
contains()方法 eg:  //*/li[@class="cate_nenu_item"]/a[contains(@href,"diannao")]<br/>
相对XPath路径写法eg:  .//*/label[@for='newstitle']/../input[@id='newstitle']
# 3.无头浏览器(Headless)
firefox 低版本不支持<br/>
Firefox 56 supports headless mode on Windows<br/>
{
  "user-agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0"
}
# 4.获取目标元素的文本方法
要获取到目标元素的text的值，需要定义一个目标元素element，然后通过element.text方法得到字符串，注意不是element.text(),这个方法是没有带小括号的。方法一是，直接把字段写入XPath表达式，如果通过该XPath能定位到元素，说明这个错误字段已经在页面显示；方法二是通过该目标元素节点，然后通过element.text得到值，在拿得到的text值取和期待的结果去字符串匹配。在自动化测试脚本开发中，采用第二个方法。