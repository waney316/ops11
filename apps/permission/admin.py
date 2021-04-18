from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from apps.permission.models import CasbinRule

# Register your models here.
@admin.register(CasbinRule)
class CasbinRuleAdmin(admin.ModelAdmin):
    # 显示
    list_display = (
        'ptype',
        'v0',
        'v1',
        'v2',
        'v3',
    )
