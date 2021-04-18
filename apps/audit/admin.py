from django.contrib import admin

from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from apps.audit.models import AuditLog

# Register your models here.
@admin.register(AuditLog)
class AuditLogAdmin(admin.ModelAdmin):
    # 显示
    list_display = (
        'pk',
        'uri',
        'method',
        'remote_ip',
        'body',
        'query_string',
        'username',
        'status_code',
        'create_time',
    )
