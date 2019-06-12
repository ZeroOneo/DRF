from django.conf.urls import url
from . import views

urlpatterns = [

   url(r'books/$', views.BooksView.as_view()),
   url(r'books/(?P<id>\d+)/$', views.ChangeView.as_view()),



]
