# http://blog.csdn.net/u011541946/article/details/70198676       参考地址
# 设置级别的日志，这个级别是最小级别，常见的有 debug<info<error，如果设置级别是Info，那么输出只显示info和error级别
import logging
import os.path
import time


class Logger(object):

    def __init__(self, logger):
        '''
        指定保证日志的路径，日志级别，调用文件将日志存入到指定的文件中
        :param logger:
        '''
        # 创建一个logger
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)

        # 创建一个handler，用来写入日志文件
        rq = time.strftime("%Y%m%d%H%M%S", time.localtime(time.time()))
        log_path = os.path.dirname(os.getcwd()) + '/logs/'
        log_name = log_path + rq + '.log'
        fh = logging.FileHandler(log_name)
        fh.setLevel(logging.INFO)

        # 创建一个handler，用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)

        # 定义handler 的输出格式
        formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        # 给logger 添加handler
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)

    def getlog(self):
        return self.logger