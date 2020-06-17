# 路径，常量管理类


import os

# ----------目录路径常量-------------
# 项目的根目录
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Conf文件夹路径
CONF_DIR = os.path.join(BASE_DIR, 'conf')
# Logs文件夹路径
LOGS_DIR = os.path.join(BASE_DIR, 'logs')
# 日志文件夹路径
TEXT_LOG = os.path.join(LOGS_DIR, 'text_log')

# ----------文件路径常量---------------
# global配置文件
GLOBAL_CONF = os.path.join(CONF_DIR, 'global.ini')
# sit配置文件
SIT_CONF = os.path.join(CONF_DIR, 'SIT.ini')
# uat配置文件
UAT_CONF = os.path.join(CONF_DIR, 'UAT.ini')
# pro配置文件
PRO_CONF = os.path.join(CONF_DIR, 'PRO.ini')

# -----------日志常量管理-----------------
# 日志输出格式
FORMATTER = '%(asctime)s-%(filename)s-%(levelname)s-%(message)s'
# 日志最大保存时间
LOG_TIME = 7
