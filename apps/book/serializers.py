from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from rest_framework.serializers import ListSerializer
from rest_framework.exceptions import ValidationError

from apps.book.models import Publisher
from apps.book.models import Book

class PublisherModelSerializer(ModelSerializer):

    def validate(self, attrs):
        print(attrs)
        if attrs.get("address"):
            address = attrs.get("address")
            if "-" not in address:
                raise ValidationError("address str must contains -")
        return attrs


    # read_only: 是否仅可读,当设置为True,该值不会被修改
    # address = serializers.CharField(read_only=True)
    # address = serializers.CharField(required=False)
    class Meta:
        model = Publisher
        # fields = "__all__"   # 序列化给前端的字段
        fields = ["id", "name", "address"]
        # read_only_fields = ["address"]
        # write_only_fields = ["id"]

        extra_kwargs = {
            "address": {
                # "write_only": True,
                "min_length": 3,
                "max_length": 10,
                "error_messages": {
                    "required": "address为必穿参数",
                    "min_length": "地址长度必须大于3位",
                    "max_length": "地址长度需要小于10位",
                }
            }
        }

class BookModelSerializer(ModelSerializer):

    class Meta:
        model = Book
        fields = "__all__"
        # depth = 1
