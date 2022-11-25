from django.db import router
from django.urls import include, path, re_path
from . import views

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('forms/', views.forms_page, name='forms_page'),
    path('quiz/', views.quiz_page, name='quiz_page'),
]