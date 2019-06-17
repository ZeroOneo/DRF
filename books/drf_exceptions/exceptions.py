from rest_framework.views import exception_handler
from rest_framework.response import Response
from django.db.models import ObjectDoesNotExist


def drf_exception_handler(exc,context):
    """
    自定义DRF处理函数，以实现DRF能够捕获非DRF异常
    :param exc:
    :param context:
    :return:
    """

    # 调用DRF原生的异常处理函数处理
    response = exception_handler(exc,context)

    # 若为空，则自定义处理
    if response:
        return response

    # 自定义处理逻辑
    if isinstance(exc,(ZeroDivisionError,ObjectDoesNotExist)):
        return Response({"result":"非DRF异常捕获"})