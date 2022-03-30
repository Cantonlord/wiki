from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # re_path(r'(?P<title>\w+)/$', views.entry, name='entry'),
    path('<str:title>/', views.entry, name='entry'),
    path('search/', views.search, name='search'),
    # path('new/')
]
