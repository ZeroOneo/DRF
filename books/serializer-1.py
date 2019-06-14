from rest_framework import serializers
from .models import *


class HeroINfoSerializer1(serializers.Serializer):
    """英雄数据序列化"""
    GENDER_CHOICES = ((0, "male"), (1, "female"))
    id = serializers.IntegerField(label="ID", read_only=True)


def check_b(value):

    if "部" not in value:
        raise serializers.ValidationError("么法的开发及阿和卡带机和扩大")


class BookInfoSerializer(serializers.Serializer):
    """图书数据序列化器"""

    id = serializers.IntegerField(label="ID", read_only=True)
    # btitle = serializers.CharField(label="名称",max_length=20,validators=[check_b])
    btitle = serializers.CharField(label="名称", max_length=20)
    bpub_date = serializers.DateField(label="发布日期", required=True)
    bread = serializers.IntegerField(label="阅读量", required=True)
    bcomment = serializers.IntegerField(label='评论量', required=False)
    image = serializers.ImageField(label='图片', required=False)

    # heroinfo_set = serializers.PrimaryKeyRelatedField(read_only=True,many=True)
    # heroinfo_set = serializers.StringRelatedField(many=True)


    # def validate_btitle(self, value):
    #
    #     if "金" not in value:
    #
    #         raise serializers.ValidationError("fdafasdfsafdsa")
    #
    #     return value

    #
    # def validate(self, attrs):
    #
    #     read = attrs["bread"]
    #
    #     if read < 20:
    #         raise serializers.ValidationError("读者这么少")
    #
    #     return attrs


    def create(self, validated_data):

        return BookInfo.objects.create(**validated_data)


    def update(self, instance, validated_data):

        instance.bread = validated_data.get("bread",instance.bread)
        instance.save()

        return instance



class HeroInfoSerializer(serializers.Serializer):
    """英雄数据序列化器"""
    GENDER_CHOICES = ((0, "male"), (1, "male"))
    id = serializers.IntegerField(label="ID", read_only=True)
    hname = serializers.CharField(max_length=20, label='名称')
    hgender = serializers.ChoiceField(choices=GENDER_CHOICES, label='性别', required=False)
    hcomment = serializers.CharField(max_length=200, label='描述信息', required=False)

    # hbook = serializers.PrimaryKeyRelatedField(read_only=True)
    # hbook = serializers.StringRelatedField()
    hbook = BookInfoSerializer(read_only=True)