from django.db import models
from django.contrib.auth.models import AbstractUser

class UserProfile(AbstractUser):
    name = models.CharField(max_length=100, verbose_name="中文名称")
    phone = models.CharField(max_length=11, verbose_name="手机号")
    staff_id = models.IntegerField(null=True, blank=True, verbose_name="员工编号")
    job_status = models.BooleanField(default=True, verbose_name="员工在职状态")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "用户"
        verbose_name_plural = verbose_name

