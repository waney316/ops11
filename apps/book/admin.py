from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from apps.book.models import Publisher
from apps.book.models import Book

# Register your models here.
@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    # 显示
    list_display = (
        'pk',
        'name',
        'address',
        'create_time',
        'update_time',
    )


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # 显示
    list_display = (
        'pk',
        'name',
        'publisher',
        'publisher_state',
        'price',
        'remark'
    )


