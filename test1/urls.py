"""test1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from rest_framework.routers import SimpleRouter, DefaultRouter
from rest_framework.documentation import include_docs_urls
from books.views import BookModelViewSet

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^docs/', include_docs_urls(title='My API title')),
    # url(r'^', include("books.urls")),



]

# 1 创建路由器对象
# 不带根视图
router = SimpleRouter()

# 带根视图
# router = DefaultRouter()

# 2 注册视图集
router.register(prefix="books", viewset=BookModelViewSet, base_name="books")

# 3 添加到主路由
urlpatterns += router.urls
