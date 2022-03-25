from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    re_path('(?P<title>\w+)/$', views.wiki, name='wiki')
]
