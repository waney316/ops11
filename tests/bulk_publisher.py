# coding: utf-8
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ops11.settings')
django.setup()


from apps.book.models import Publisher



# ps = []
# for x in range(200, 10000):
#     data = {
#         "name": f"new{x}",
#         "address": "beijing",
#     }
#     p = Publisher(**data)
#     ps.append(p)

# 批量创建
# Publisher.objects.bulk_create(ps)
print(Publisher.objects.count())
# 批量删除
# Publisher.objects.filter(pk__lt=200).delete()
print(Publisher.objects.count())