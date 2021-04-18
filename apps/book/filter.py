# coding: utf-8
import django_filters
from apps.book.models import Book
from apps.user.models import UserProfile

# 自定义过滤器,字段过滤
class BookFilter(django_filters.FilterSet):

    class Meta:
        model = Book
        fields = {
            "name": ["exact"],
            "price": ["lt", "gt"],
            "publisher__name": ["exact"],
            "authors__username": ["exact"]
        }


class CustomBookFilter(django_filters.FilterSet):
    # 自定义搜索字段
    authors__username = django_filters.CharFilter(method="my_custom_filter")


    class Meta:
        model = Book
        fields = ["authors__username"]

    def my_custom_filter(self, queryset, field_name,value):
        '''

        :param queryset: queryset,返回当前序列化后所有数据
        :param field_name: 字段名，查询的字段名
        :param value: 查询时的值，查询时写入的值
        :return:
        '''
        print(queryset)
        print(field_name)
        print(value)
        # 根据用户名称过滤书籍
        try:
            u = UserProfile.objects.get(username=value)
        except UserProfile.DoesNotExist:
            return queryset.none()

        return u.book_set.all()


