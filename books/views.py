from rest_framework import serializers
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


# -------------APIView--------------


class BookListView(APIView):
    """APIview"""

    def get(self, request):
        books = BookInfo.objects.all()

        serializer = BookInfoModelSerializer(instance=books, many=True)

        return Response(serializer.data)


# ------------GenericAPIView----------

class BooksGenericAPIView(GenericAPIView):
    # 指明当前类视图所使用的序列化器
    serializer_class = BookInfoModelSerializer

    # 指明当前类试图所使用的数据集
    queryset = BookInfo.objects.all()

    # 使用GenericAPIView实现多条数据序列化处理逻辑
    def get(self, request):
        # 1 获得多个对象
        books = self.get_queryset()

        # 2 获得序列器对象
        bs = BookInfoModelSerializer(instance=books, many=True)

        # 3 返回响应
        return Response(bs.data, status=HTTP_200_OK)

    # 新建数据  url books/   json
    def post(self, request):
        # 1 获取请求参数
        book = request.data

        # 2 构建序列器对象
        bs = self.get_serializer(data=book)

        # # 3 校验
        # if bs.is_valid():
        #
        #     # 4 保存
        #     bs.save()
        #
        #     # 5 序列化返回
        #     return Response(bs.data,status=HTTP_201_CREATED)
        #
        # raise serializers.ValidationError("数据校验失败")

        # 3 校验
        bs.is_valid(raise_exception=True)

        # 4 保存
        bs.save()

        # 5 序列化返回
        return Response(bs.data, status=HTTP_201_CREATED)


class BookGenericAPIView(GenericAPIView):
    queryset = BookInfo.objects.all()
    serializer_class = BookInfoModelSerializer

    def get(self, request, pk):
        """查询单一数据对象"""

        # 1 获得单一数据对象
        book = self.get_object()

        # 2 获得序列化器对象
        bs = self.get_serializer(book)

        # 3 序列化返回
        return Response(bs.data, status=HTTP_200_OK)

    def put(self, request, pk):
        """更新单一对象"""

        # 1 获取前端数据
        bookinfo = request.data

        # 2 获取更新的单一数据对象
        book = self.get_object()

        # 3 更新
        bs = self.get_serializer(instance=book, data=bookinfo)

        bs.is_valid(raise_exception=True)
        bs.save()

        # 4 序列化返回
        return Response(bs.data)

    def patch(self, request, pk):
        """部分更新"""

        # 1 获取前端数据
        bookinfo = request.data

        # 2 获取单一对象
        book = self.get_object()

        # 3 获取序列化器对象
        bs = self.get_serializer(instance=book, data=bookinfo, partial=True)

        # 4 数据校验
        bs.is_valid(raise_exception=True)

        # 5 更新保存
        bs.save()

        # 6 序列化返回
        return Response(bs.data, status=HTTP_201_CREATED)

    def delete(self, request, pk):
        """删除单一对象"""

        # 1 获取单一对象
        book = self.get_object()

        # 2 删除
        book.delete()

        # 3 返回响应
        return Response({}, status=HTTP_204_NO_CONTENT)


# ------------mixin----------------


class BooksModelMixinView(CreateModelMixin, ListModelMixin, GenericAPIView):
    # 指明当前类视图所使用的序列化器
    serializer_class = BookInfoModelSerializer

    # 指明当前类试图所使用的数据集
    queryset = BookInfo.objects.all()

    # 使用GenericAPIView实现多条数据序列化处理逻辑
    def get(self, request):
        return self.list(request)

    # 新建数据  url books/   json
    def post(self, request):
        return self.create(request)


class BookModelMixinView(DestroyModelMixin, UpdateModelMixin, RetrieveModelMixin, GenericAPIView):
    queryset = BookInfo.objects.all()
    serializer_class = BookInfoModelSerializer

    def get(self, request, pk):
        """查询单一数据对象"""
        return self.retrieve(request, pk)

    def put(self, request, pk):
        """更新单一对象"""
        return self.update(request, pk)

    def patch(self, request, pk):
        """部分更新"""

        return self.partial_update(request, pk)

    def delete(self, request, pk):
        """删除单一对象"""
        return self.partial_update(request, pk)


# ------------ListAPIView----------------


class BooksListAPIView(ListAPIView, CreateAPIView):
    # 指明当前类视图所使用的序列化器
    serializer_class = BookInfoModelSerializer

    # 指明当前类试图所使用的数据集
    queryset = BookInfo.objects.all()


class BookListAPIView(RetrieveAPIView, UpdateAPIView, DestroyAPIView):
    queryset = BookInfo.objects.all()
    serializer_class = BookInfoModelSerializer


# ------------ModelViewSet----------------


class BookModelViewSet(ModelViewSet):
    queryset = BookInfo.objects.all()
    serializer_class = BookInfoModelSerializer

    def lastest(self, request):
        book = BookInfo.objects.latest("bpub_date")
        bs = BookInfoModelSerializer(book)

        return Response(bs.data)
