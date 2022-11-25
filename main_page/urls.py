from django.db import router
from django.urls import include, path, re_path
from . import views

urlpatterns = [
    path('', views.main_home, name='main_page'),
]