import datetime
# 获取当前时间
now = datetime.datetime.now()
# 获取今天零点
zeroToday = now - datetime.timedelta(hours=now.hour, minutes=now.minute, seconds=now.second, microseconds=now.microsecond)
# 获取23:59:59
lastToday = zeroToday + datetime.timedelta(hours=23, minutes=59, seconds=59)
# 获取前一天的当前时间
yesterdayNow = now - datetime.timedelta(hours=23, minutes=59, seconds=59)
# 获取明天的当前时间
tomorrowNow = now + datetime.timedelta(hours=23, minutes=59, seconds=59)
# 获取2小时之前的数据
hourbefore = now - datetime.timedelta(hours=3)

