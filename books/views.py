from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import serializers
from rest_framework.filters import OrderingFilter
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import *
from rest_framework.viewsets import ModelViewSet
from .models import BookInfo
from .serializer import BookInfoModelSerializer
from rest_framework.generics import GenericAPIView, ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, \
    DestroyAPIView
from rest_framework.mixins import CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin, \
    DestroyModelMixin
from rest_framework.decorators import action
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAdminUser, AllowAny
from rest_framework.throttling import UserRateThrottle, ScopedRateThrottle, AnonRateThrottle
from django_filters import FilterSet
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination


# # -------------APIView--------------
#
#
# class BookListView(APIView):
#     """APIview"""
#
#     def get(self, request):
#         books = BookInfo.objects.all()
#
#         serializer = BookInfoModelSerializer(instance=books, many=True)
#
#         return Response(serializer.data)
#
#
# ------------GenericAPIView----------
#
# class BooksGenericAPIView(GenericAPIView):
#     # 指明当前类视图所使用的序列化器
#     serializer_class = BookInfoModelSerializer
#
#     # 指明当前类试图所使用的数据集
#     queryset = BookInfo.objects.all()
#
#     # 使用GenericAPIView实现多条数据序列化处理逻辑
#     def get(self, request):
#         # 1 获得多个对象
#         books = self.get_queryset()
#
#         # 2 获得序列器对象
#         bs = BookInfoModelSerializer(instance=books, many=True)
#
#         # 3 返回响应
#         return Response(bs.data, status=HTTP_200_OK)
#
#     # 新建数据  url books/   json
#     def post(self, request):
#         # 1 获取请求参数
#         book = request.data
#
#         # 2 构建序列器对象
#         bs = self.get_serializer(data=book)
#
#         # # 3 校验
#         # if bs.is_valid():
#         #
#         #     # 4 保存
#         #     bs.save()
#         #
#         #     # 5 序列化返回
#         #     return Response(bs.data,status=HTTP_201_CREATED)
#         #
#         # raise serializers.ValidationError("数据校验失败")
#
#         # 3 校验
#         bs.is_valid(raise_exception=True)
#
#         # 4 保存
#         bs.save()
#
#         # 5 序列化返回
#         return Response(bs.data, status=HTTP_201_CREATED)
#
#
# class BookGenericAPIView(GenericAPIView):
#     queryset = BookInfo.objects.all()
#     serializer_class = BookInfoModelSerializer
#
#     def get(self, request, pk):
#         """查询单一数据对象"""
#
#         # 1 获得单一数据对象
#         book = self.get_object()
#
#         # 2 获得序列化器对象
#         bs = self.get_serializer(book)
#
#         # 3 序列化返回
#         return Response(bs.data, status=HTTP_200_OK)
#
#     def put(self, request, pk):
#         """更新单一对象"""
#
#         # 1 获取前端数据
#         bookinfo = request.data
#
#         # 2 获取更新的单一数据对象
#         book = self.get_object()
#
#         # 3 更新
#         bs = self.get_serializer(instance=book, data=bookinfo)
#
#         bs.is_valid(raise_exception=True)
#         bs.save()
#
#         # 4 序列化返回
#         return Response(bs.data)
#
#     def patch(self, request, pk):
#         """部分更新"""
#
#         # 1 获取前端数据
#         bookinfo = request.data
#
#         # 2 获取单一对象
#         book = self.get_object()
#
#         # 3 获取序列化器对象
#         bs = self.get_serializer(instance=book, data=bookinfo, partial=True)
#
#         # 4 数据校验
#         bs.is_valid(raise_exception=True)
#
#         # 5 更新保存
#         bs.save()
#
#         # 6 序列化返回
#         return Response(bs.data, status=HTTP_201_CREATED)
#
#     def delete(self, request, pk):
#         """删除单一对象"""
#
#         # 1 获取单一对象
#         book = self.get_object()
#
#         # 2 删除
#         book.delete()
#
#         # 3 返回响应
#         return Response({}, status=HTTP_204_NO_CONTENT)
#
#
# # ------------mixin----------------
#
#
# class BooksModelMixinView(CreateModelMixin, ListModelMixin, GenericAPIView):
#     # 指明当前类视图所使用的序列化器
#     serializer_class = BookInfoModelSerializer
#
#     # 指明当前类试图所使用的数据集
#     queryset = BookInfo.objects.all()
#
#     # 使用GenericAPIView实现多条数据序列化处理逻辑
#     def get(self, request):
#         return self.list(request)
#
#     # 新建数据  url books/   json
#     def post(self, request):
#         return self.create(request)
#
#
# class BookModelMixinView(DestroyModelMixin, UpdateModelMixin, RetrieveModelMixin, GenericAPIView):
#     queryset = BookInfo.objects.all()
#     serializer_class = BookInfoModelSerializer
#
#     def get(self, request, pk):
#         """查询单一数据对象"""
#         return self.retrieve(request, pk)
#
#     def put(self, request, pk):
#         """更新单一对象"""
#         return self.update(request, pk)
#
#     def patch(self, request, pk):
#         """部分更新"""
#
#         return self.partial_update(request, pk)
#
#     def delete(self, request, pk):
#         """删除单一对象"""
#         return self.partial_update(request, pk)
#
#
# # ------------ListAPIView----------------
#
#
# class BooksListAPIView(ListAPIView, CreateAPIView):
#     # 指明当前类视图所使用的序列化器
#     serializer_class = BookInfoModelSerializer
#
#     # 指明当前类试图所使用的数据集
#     queryset = BookInfo.objects.all()
#
#
# class BookListAPIView(RetrieveAPIView, UpdateAPIView, DestroyAPIView):
#     queryset = BookInfo.objects.all()
#     serializer_class = BookInfoModelSerializer


# ------------ModelViewSet----------------


class Mypage2(PageNumberPagination):
    """自定义分页"""
    page_size_query_param = "page_size"
    page_query_param = "page"
    page_size = 2
    max_page_size = 10000


class Mypage(PageNumberPagination):
    """重写分页"""
    page_size_query_param = "page_size"
    max_page_size = 3


class MyLimit(LimitOffsetPagination):
    """limit   offset 重写"""
    limit_query_param = "limit"
    max_limit = 5
    offset_query_param = "offset"


class MyFilterSet(FilterSet):
    """自定义过滤"""

    class Meta:
        model = BookInfo
        fields = ["btitle", "bread"]
        # fields = {
        #     "btitle": ["exact", "contains", "startswith"],
        #     "bread": ["exact", "gte"]
        # }


class BookModelViewSet(ModelViewSet):
    """
    list:
    返回所有哦图书信息

    create:
    新建图书


    """

    queryset = BookInfo.objects.all()
    serializer_class = BookInfoModelSerializer

    # 身份认证
    authentication_classes = [SessionAuthentication]

    # 权限认证
    permission_classes = [AllowAny]

    # 限流设置
    throttle_classes = [UserRateThrottle]

    # 限流依据
    throttle_scope = "user"

    # 过滤后端
    filter_backends = [DjangoFilterBackend, OrderingFilter]

    # 设置过滤依据
    # filterset_fields = ["btitle","bread"]

    # 自定义过滤依据条件（类）
    filterset_class = MyFilterSet

    # 自定义分页类
    # pagination_class = Mypage

    # pagination_class = Mypage2

    # pagination_class = MyLimit

    # 关闭分页
    # pagination_class = None

    # # 指定请求方法绑定 以添加路由
    # @action(methods=["get"], detail=False)
    # def lastest(self, request):
    #     book = BookInfo.objects.latest("bpub_date")
    #     bs = BookInfoModelSerializer(book)
    #
    #     return Response(bs.data)
    #
    # # 修改阅读量
    # @action(methods=["patch"], detail=True)
    # def read(self, request, pk):
    #     book = BookInfo.objects.get(id=pk)
    #     book.bread = book, request.data.get("bread")
    #     book.save()
    #     return Response({"bread": book.bread}, status=HTTP_202_ACCEPTED)
