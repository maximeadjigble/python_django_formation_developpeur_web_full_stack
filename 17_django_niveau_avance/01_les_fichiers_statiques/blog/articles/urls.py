from django.contrib import admin
from django.urls import path, include

from . import views

app_name = "articles"

urlpatterns = [
    path('', views.articles_view, name='articles'),
    path('<slug:slug>/', views.article_view, name='article')
]
