# coding: utf-8
# 自定义中间件
import datetime
import json
from common import std_format
from django.template.response import TemplateResponse
from django.utils.deprecation import MiddlewareMixin
from apps.audit.models import AuditLog

from rest_framework.authentication import BaseAuthentication
from rest_framework.response import Response
class AuditMiddleware(MiddlewareMixin):
    pk = None
    def process_request(self, request):
        """
        将请求的数据封装存入数据库
        :param request: request请求对象,包含request.META和request.body
        :return:
        """
        # 如果请求uri为admin后台不记录
        if request.META.get('PATH_INFO').startswith('/admin'):
            return
        data = {
            "uri": request.META.get('PATH_INFO'),
            "method": request.META.get('REQUEST_METHOD'),
            "query_string": request.META.get("QUERY_STRING"),
            "username": request.META.get("USER"),
            "remote_ip": request.META.get("REMOTE_ADDR")

        }
        # 记录post或put请求主体
        try:
            data['body'] = json.loads(request.body)
        except:
            data['body'] = ""

        log_obj = AuditLog.objects.create(**data)
        self.pk = log_obj.pk

        # print(std_format.json_format(request.META))
        print("this is process request", datetime.datetime.now())


    def process_response(self, request, response):
        try:
            # 通过pk查询到该次请求的状态吗
            response_obj = AuditLog.objects.get(pk=self.pk)
        except AuditLog.DoesNotExist:
            return response

        # TemplateResponse/HttpResponse: admin响应类型
        if type(response) == Response:
            code = response.data.get("code")
        else:
            code = -1
        response_obj.status_code = code
        response_obj.save()

        print("this is process response", datetime.datetime.now())
        return response

    def process_view(self, request, callback, callback_args, callback_kwargs):
        print("this is process view", datetime.datetime.now())


    def process_exception(self, request, exception):
        print("this is exceptipon process", datetime.datetime.now())

    def process_template_response(self, request, response):
        print("this is template response process", datetime.datetime.now())
        return response