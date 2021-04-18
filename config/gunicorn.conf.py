import os
import sys
import multiprocessing
BASE_DIR = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
sys.path.append(BASE_DIR)
LOG_DIR = os.path.join(BASE_DIR, 'logs')
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)
# 绑定的ip与端⼝
port = 8000
bind = f"0.0.0.0:{port}"
# 以守护进程的形式后台运⾏
daemon = True
# 最⼤挂起的连接数，64-2048
backlog = 512
# 超时
timeout = 30
# 调试状态
debug = True
# gunicorn要切换到的⽬的⼯作⽬录
chdir = BASE_DIR
# ⼯作进程类型(默认的是 sync 模式，还包括 eventlet, gevent, or tornado, gthread,gaiohttp)
worker_class = 'sync'

# ⼯作进程数
workers = multiprocessing.cpu_count()
# 指定每个⼯作进程开启的线程数
threads = 1
# ⽇志级别，这个⽇志级别指的是错误⽇志的级别(debug、info、warning、error、critical)，⽽访问⽇志的级别⽆法设置
loglevel = 'debug'
# ⽇志格式
access_log_format = '%(t)s %(p)s %(h)s "%(r)s" %(s)s %(L)s %(b)s %(f)s" "%(a)s"'
# 其每个选项的含义如下：
'''
h remote address
l '-'
u currently '-', may be user name in future releases
t date of the request
r status line (e.g. ``GET / HTTP/1.1``)
s status
b response length or '-'
f referer
a user agent
T request time in seconds
D request time in microseconds
L request time in decimal seconds
p process ID
'''
# # 访问⽇志⽂件
# accesslog = os.path.join(LOG_DIR, 'gunicorn_access.log')
# # 错误⽇志⽂件
# errorlog = os.path.join(LOG_DIR, 'gunicorn_error.log')
# # 访问⽇志⽂件，"-" 表示标准输出
# accesslog = "-"
# # 错误⽇志⽂件，"-" 表示标准输出
# errorlog = "-"