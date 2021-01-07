import time
import requests
import json

from datetime import datetime, timedelta
from jd_seckill.config import global_config

buy_time = time.strptime(global_config.getRaw('config', 'buy_time'),"%H:%M:%S.%f")
now = int(time.time())
#转换为其他日期格式,如:"%Y-%m-%d %H:%M:%S"
local_now = time.localtime(now)
time_tody = time.strftime("%Y-%m-%d", local_now)
time_tody_delta = (datetime.fromisoformat(time_tody) + timedelta(hours=buy_time.tm_hour,minutes=buy_time.tm_min,seconds=buy_time.tm_sec))
print(time_tody_delta)

print(buy_time)