# posts/urls.py
from django.urls import path

from . import views

urlpatterns = [
    # Главная страница
    path('', views.index),
    # Подробная информация поста
    path('group/<slug:slug>/', views.posts_group),
]
