from django.shortcuts import render
from django.http.response import HttpResponse
from django.views import View

from apps.book.models import Publisher
from apps.book.models import Book
from apps.book.serializers import PublisherModelSerializer
from apps.book.serializers import BookModelSerializer
from apps.book.filter import BookFilter, CustomBookFilter
from django_filters import rest_framework as filters

from rest_framework.views import APIView
from rest_framework.exceptions import NotFound
from rest_framework.generics import GenericAPIView, ListAPIView, CreateAPIView, ListCreateAPIView, DestroyAPIView, \
    UpdateAPIView, RetrieveAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.renderers import AdminRenderer, JSONRenderer, BrowsableAPIRenderer
from rest_framework.parsers import JSONParser, FormParser, MultiPartParser
from rest_framework_yaml.renderers import YAMLRenderer
from rest_framework_csv.renderers import CSVRenderer
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.authentication import TokenAuthentication, BaseAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie, vary_on_headers

from base.reponse import JSONAPIResponse
from base.pagination import CustomPagination, CustomLimitPagination
from base.throtting import CustomThrott
from base.views import BaseModelViewSet
from base.permission import ApiRBACPermission


# FBV
def PrintHello(request):
    return HttpResponse("hello django")


# CBV
class PublishView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("CBV: get")

    def post(self, request, *args, **kwargs):
        return HttpResponse("View post")

    def put(self, request, *args, **kwargs):
        return HttpResponse("View put")

    def delete(self, request, *args, **kwargs):
        return HttpResponse("View delete")


# DRF VIEW
class PublisherApiView(APIView):
    # parser_classes = [FormParser]
    renderer_classes = [JSONRenderer, AdminRenderer, BrowsableAPIRenderer, YAMLRenderer, CSVRenderer]
    # authentication_classes = [TokenAuthentication, ]
    # 使用jwt token
    # authentication_classes = [TokenAuthentication]
    # 使用casbin控制路径权限访问
    # authentication_classes = [JSONWebTokenAuthentication,]
    permission_classes = [ApiRBACPermission,]
    #S

    # permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return Publisher.objects.get(pk=pk)
        except Publisher.DoesNotExist:
            raise NotFound()

    # @method_decorator(cache_page(60 * 60 * 2))
    # @method_decorator(vary_on_cookie)
    def get(self, request, format=None, *args, **kwargs):
        # /api/v1/book/publisher
        if kwargs.get("pk"):
            # 查看单条数据
            p = self.get_object(kwargs['pk'])
            data = p.serializer()
        else:
            # 查询全部数据
            ps = Publisher.objects.all()  # queryset []
            data = [p.serializer() for p in ps]
        return JSONAPIResponse(code=0, data=data, message=None)

    def post(self, request):
        data = request.data
        try:
            p = Publisher.objects.create(**data)
        except Exception as e:
            return  JSONAPIResponse(code=-1, data=None, message=e.args)
        return JSONAPIResponse(code=0, data=p.serializer(), message=None)

    def put(self, request, *args, **kwargs):
        data = request.data

        count = Publisher.objects.filter(pk=kwargs['pk']).update(**data)
        # 受影响的行数
        if count == 0:
            return JSONAPIResponse(code=-1, data=None, message="Update fail, please check.")
        else:
            return JSONAPIResponse(code=0, data=None, message=f"{count} record is updated.")

    def delete(self, request, *args, **kwargs):
        p = self.get_object(kwargs['pk'])
        p.delete()
        return JSONAPIResponse(code=0, data=None, message="Delete ok.")


# get all
class PublisherListAPIView(ListAPIView):
    queryset = Publisher.objects.all()
    serializer_class = PublisherModelSerializer


# create data
class PublisherCreateAPIView(CreateAPIView):
    queryset = Publisher.objects.all()
    serializer_class = PublisherModelSerializer


# list create
class PublisherListCreateAPIView(ListCreateAPIView):
    queryset = Publisher.objects.all()
    serializer_class = PublisherModelSerializer


# delete data
class PublisherDestroyAPIView(DestroyAPIView):
    queryset = Publisher.objects.all()
    serializer_class = PublisherModelSerializer


# update data
class PublisherUpdateAPIView(UpdateAPIView):
    queryset = Publisher.objects.all()
    serializer_class = PublisherModelSerializer


class PublisherRetrieveAPIView(RetrieveAPIView):
    queryset = Publisher.objects.all()
    serializer_class = PublisherModelSerializer


#### ViewSet  需要搭配Router
class PublisherModelViewSet(ModelViewSet):
    queryset = Publisher.objects.all()
    serializer_class = PublisherModelSerializer

    ## 分页
    # pagination_class = CustomPagination
    pagination_class = CustomLimitPagination

    ## 过滤器
    # 查找
    filter_backends = [SearchFilter, OrderingFilter]
    # 模糊匹配
    # search_fields = ["name", "address"]
    # 精准匹配
    search_fields = ["=name"]

    # 排序
    ordering_fields = ["id", "create_time", "update_time"]

    @action(methods=['get'], detail=False, url_path='change-password', url_name='change_password')
    def set_password(self, request):
        print("enter action")
        return JSONAPIResponse(code=0, data={"info": "action"}, message=None)


class BookModelViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookModelSerializer

    ## 过滤器
    filter_backends = [SearchFilter, filters.DjangoFilterBackend]
    # 模糊匹配
    search_fields = ["name", "publisher__name"]

    # django-filter 过滤
    # filterset_fields = ["name", "price", "publisher_state"]
    # filterset_class = BookFilter
    filterset_class = CustomBookFilter
    # 限流
    throttle_classes = [CustomThrott]

    # 禁用delete请求
    # http_method_names = ["get", "post"]

    # def destroy(self, request, *args, **kwargs):
    #     return JSONAPIResponse(code=-1, data=None, message="DELETA not allowed")


# 对返回的book数据统一封装
class BookBaseModelViewSet(BaseModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookModelSerializer
    search_fields = ["name", "publisher__name"]
    http_method_names = ["get", ]
