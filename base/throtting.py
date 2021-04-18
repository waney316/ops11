# coding: utf-8

# 限流
from rest_framework.throttling import AnonRateThrottle

class CustomThrott(AnonRateThrottle):
     THROTTLE_RATES = {
         # 匿名用户限制每分钟请求三次
        'anon': '20/m',
    }