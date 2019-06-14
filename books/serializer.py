from rest_framework import serializers
from .models import *


class BookInfoModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookInfo

        # 序列化所有字段
        fields = "__all__"

        # 指定字段序列化
        # fields = ["btitle","bpub_date"]

        # 不序列化的字段
        # exclude = ["btitle"]

        # 指定字段只读属性 只能序列化  不能反序列化
        # read_only_fields = ["btitle", "bpub_date"]

        # 字段的额外约束条件
        # extra_kwargs = {
        #     "bread": {"min_value": 0, "required": True}
        # }
