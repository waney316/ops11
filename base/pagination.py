# coding: utf-8
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination

class CustomPagination(PageNumberPagination):
    # 定义默认查询没页显示几个
    page_size = 3
    # 定义page_size查询参数
    page_size_query_param = "page_size "
    page_query_param = "page"
    # 每页显示最大值
    max_page_size = 10

class CustomLimitPagination(LimitOffsetPagination):
    # limit:限制返回的条数，offset：从初始位置的偏移量
    default_limit = 2