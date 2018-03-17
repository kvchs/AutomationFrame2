# makeSuite()方法，一次性加载一个类文件下所有测试用例到suite中去

# import unittest
# from test.test_get_page_title import GetPageTitle
# from test.news_nba_view import ViewNBANews
#
#
# suite = unittest.TestSuite()
# suite.addTest(ViewNBANews("test_view_nba_views"))
# suite.addTest(GetPageTitle("test_get_title"))
#
# if __name__ == '__main__':
#     runner = unittest.TextTestRunner()
#     runner.run(suite)
#


# from test.test_get_page_title import GetPageTitle
# from test.news_nba_view import ViewNBANews

# suite = unittest.TestSuite(unittest.makeSuite(GetPageTitle))
# # suite(unittest.makeSuite(GetPageTitle))
# NOTE :测试用例类.py文件名也需test开头

import HTMLTestRunner
import os
import unittest
import time


report_path = os.path.dirname(os.path.abspath(".")) + '/test_report/'
now_time = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime(time.time()))
htmlFile = report_path + now_time + "template.html"
fp = open(htmlFile, 'wb')
suite = unittest.TestLoader().discover("test")

if __name__ == '__main__':
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title="auto report", description="sanity test")
    runner.run(suite)
