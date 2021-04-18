from django.db import models

from django.db import models
from base.model import BaseModel


# Create your models here.

class AuditLog(BaseModel):
    uri = models.CharField(max_length=254, db_index=True, verbose_name="URI", help_text='uri')
    method = models.CharField(max_length=20, db_index=True, verbose_name="请求方式", help_text='请求方式')
    query_string = models.CharField(max_length=254, null=True, verbose_name="URL请求参数", help_text='URL请求参数')
    body = models.TextField(verbose_name="请求Body数据", help_text="请求Body数据")
    remote_ip = models.CharField(max_length=50, verbose_name="远程主机IP", help_text="远程主机IP")
    username = models.CharField(max_length=50, verbose_name="请求用户", help_text="请求用户")
    status_code = models.IntegerField(null=True, blank=True, verbose_name="请求状态码", help_text="请求状态码")
    # create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间", help_text="创建时间")

    def __str__(self):
        return self.uri

    class Meta:
        verbose_name = "API 审计"
        verbose_name_plural = verbose_name
