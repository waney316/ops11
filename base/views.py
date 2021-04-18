# coding: utf-8
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import OrderingFilter, SearchFilter
from django_filters import rest_framework as filters

from base.reponse import JSONAPIResponse
from base.pagination import CustomPagination

class BaseModelViewSet(ModelViewSet):
    pagination_class = CustomPagination
    filter_backends = [OrderingFilter, SearchFilter, filters.DjangoFilterBackend]
    search_fields = []
    filterset_fields = []
    filterset_class = None
    throttle_classes = []


    # 重写ListModelMixin 方法
    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        return JSONAPIResponse(code=0, data=response.data, message=None)

    # 单条获取
    def retrieve(self, request, *args, **kwargs):
        response = super().retrieve(request, *args, **kwargs)
        return JSONAPIResponse(code=0, data=response.data, message=None)

    # 删除
    def destroy(self, request, *args, **kwargs):
        response = super().destroy(request, *args, **kwargs)
        return JSONAPIResponse(code=0, data=response.data, message=None)

    # 新增
    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return JSONAPIResponse(code=0, data=response.data, message=None)

    # 全部更新put
    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        return JSONAPIResponse(code=0, data=response.data, message=None)

    # 局部更新
    def partial_update(self, request, *args, **kwargs):
        response = super().partial_update(request, *args, **kwargs)
        return JSONAPIResponse(code=0, data=response.data, message=None)
