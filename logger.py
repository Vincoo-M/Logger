#!/usr/bin/env python
# -*- codeing:utf-8 -*-
'''
基于logging和colorlog模块编写的自定义logger模块
按照Log日志等级，在控制台显示不同的等级颜色
创建Logger对象即可使用，无需配置
'''
__author__ = 'Vincoo'
__version__ = '1.0'
__date__ = 'Sep 30, 2020'

import os
import colorlog
import logging
from time import strftime, localtime

LOG_COLORS_CONFIG = {
    # black, red, green, yellow, blue, purple, cyan,  white
    'DEBUG': 'bold_white',
    'INFO': 'bold_blue',
    'WARNING': 'bold_yellow',
    'ERROR': 'bold_red',
    'CRITICAL': 'bold_black,bg_red',
}
DEFAULT_FMT = "[%(asctime)s] [%(levelname)-8s] [form:/%(module)s/%(funcName)s] [line:%(lineno)d]  Message: %(message)s"
DEFAULT_DATEFMT = "%Y-%m-%d %H:%M:%S"
DEFAULT_LOG_PATH = r'./log/' + strftime('%Y%m%d', localtime()) + '.log'


class Logger(object):
    DEBUG = 10
    INFO = 20
    WARNING = 30
    ERROR = 40
    CRITICAL = 50
    DEFAULT_LEVEL = WARNING

    _instance = None
    _first_init = False

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, name=None, level=DEFAULT_LEVEL, tofile=False, fmt=DEFAULT_FMT, datefmt=DEFAULT_DATEFMT):
        '''
        :param name: 创建logger, 默认为空-root
        :param level: 设置logger日志等级, 默认为debug
        :param tofile: 设置是否将日志输出到文件, 默认路径 ./log/xxxxxx.log
        :param fmt: 设置日志格式
        :param datefmt: 设置时间格式
        '''
        cls = type(self)
        if not cls._first_init:
            self.logger = logging.getLogger() if name is None else logging.getLogger(name)
            self.logger.setLevel(level)
            self.fh = None
            file_formatter = logging.Formatter(fmt=fmt, datefmt=datefmt)  # 写入文件的日志格式
            fmt = '%(log_color)s' + fmt  # 在fmt前添加颜色格式
            console_formatter = colorlog.ColoredFormatter(fmt, datefmt=datefmt, log_colors=LOG_COLORS_CONFIG)  # 控制台打印的日志格式
            # 创建写入文件的日志格式
            # 向Handler中添加
            if tofile:
                dirname = os.path.dirname(DEFAULT_LOG_PATH)  # 获取文件夹路径
                if not os.path.exists(dirname):
                    print('No such file or directory: ' + dirname)
                    print('Create directory: ' + dirname)
                    os.mkdir(dirname)
                self.fh = logging.FileHandler(DEFAULT_LOG_PATH, encoding="utf-8", mode='a')
                self.fh.setFormatter(file_formatter)
                self.logger.addHandler(self.fh)

            # 创建控制台的日志格式
            # 向Handler中添加
            self.ch = logging.StreamHandler()
            self.ch.setFormatter(console_formatter)
            self.logger.addHandler(self.ch)

    def get_logger(self):
        return self.logger


if __name__ == '__main__':
    LOG = Logger().get_logger()
    LOG.debug('debug')
    LOG.info('info')
    LOG.warning('warning')
    LOG.error('error')
    LOG.fatal('fatal')
