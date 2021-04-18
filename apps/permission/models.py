from django.db import models

from base.model import BaseModel


class CasbinRule(BaseModel):
    ptype = models.CharField(max_length=255, verbose_name="权限类型")  # p | g
    v0 = models.CharField(max_length=255, verbose_name="角色")
    v1 = models.CharField(max_length=255, verbose_name="请求路径")
    v2 = models.CharField(max_length=255, blank=True, null=True, verbose_name="请求方法")
    v3 = models.CharField(max_length=255, blank=True, null=True)
    v4 = models.CharField(max_length=255, blank=True, null=True)
    v5 = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'casbin_rule'

    def __str__(self):
        text = self.ptype

        if self.v0:
            text = text + ', ' + self.v0
        if self.v1:
            text = text + ', ' + self.v1
        if self.v2:
            text = text + ', ' + self.v2
        if self.v3:
            text = text + ', ' + self.v3
        if self.v4:
            text = text + ', ' + self.v4
        if self.v5:
            text = text + ', ' + self.v5
        # p, zhengyansheng, /api/v1/book/publisher, GET
        # p, zhengyansheng, /api/v1/book/publisher, (GET)|(POST)
        return text

    def __repr__(self):
        return '<CasbinRule {}: "{}">'.format(self.id, str(self))