# import os
# # 获取当前项目的根目录的相对路径
# print(os.path.dirname(os.path.abspath('.')))

import configparser
import os


class TestReadConfigFile(object):

    def get_value(self):
        root_dir = os.path.dirname(os.path.abspath('.'))
        print(root_dir)

        config = configparser.ConfigParser()
        file_path = os.path.dirname(os.path.abspath('.')) + r'\config\config.ini'
        print(file_path)
        config.read(file_path, 'utf-8')

        browser = config.get("browserType", "browserName")
        url = config.get("testURL", "URL")

        return browser,url   # 返回的是一个元组


data = TestReadConfigFile()
date = data.get_value()
print(date)


