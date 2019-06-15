from django.conf.urls import url
from . import views

urlpatterns = [

   url(r'^books1/$', views.BookListView.as_view()),

   url(r'^books2/$', views.BooksGenericAPIView.as_view()),

   url(r'^books3/(?P<pk>\d+)/$', views.BookGenericAPIView.as_view()),

   url(r'^books4/$', views.BooksModelMixinView.as_view()),

   url(r'^books5/(?P<pk>\d+)/$', views.BookModelMixinView.as_view()),

   url(r'^books6/$', views.BooksListAPIView.as_view()),

   url(r'^books7/(?P<pk>\d+)/$', views.BookListAPIView.as_view()),

   url(r'^books8/latest/$', views.BookModelViewSet.as_view({'get': 'latest'})),
]