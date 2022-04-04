from unicodedata import name
from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:title>/', views.entry, name='entry'),
    path('search', views.search, name='search'),
    path('create', views.create, name='create'),
    path('<str:title>/edit', views.edit, name='edit'),
    
    # re_path(r'(?P<title>\w+)/$', views.entry, name='entry'),
]
