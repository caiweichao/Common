import configparser
import os

from util import contants
from util.logs import log


class ConfigLoader:

    def __init__(self):
        # 创建读取配置文件实例
        self.conf = configparser.ConfigParser()
        # 加载配置文件
        self.conf.read(filenames=contants.GLOBAL_CONF, encoding='utf-8')
        if self.conf.get('env', 'profile') == 'PRO':
            self.conf.read(filenames=contants.PRO_CONF, encoding='utf-8')
        elif self.conf.get('env', 'profile') == 'UAT':
            self.conf.read(filenames=contants.UAT_CONF, encoding='utf-8')
        elif self.conf.read('env', 'profile') == 'SIT':
            self.conf.read(filenames=contants.SIT_CONF, encoding='utf-8')

    def get(self, section, option):  # 返回str类型的值
        # 根据section，option 来取到配置的值
        return self.conf.get(section, option)

    def getboolean(self, section, option):  # 返回str类型的值
        # 根据section，option 来取到配置的值
        return self.conf.getboolean(section, option)

    def getint(self, section, option):  # 返回str类型的值
        # 根据section，option 来取到配置的值
        return self.conf.getint(section, option)

    def getfloat(self, section, option):  # 返回float类型的值
        # 根据section，option 来取到配置的值
        return self.conf.getfloat(section, option)

if __name__ == '__main__':
    pass