from django.contrib import admin
from django.urls import path

from . import views


urlpatterns = [
    path('', views.utilisateurs_view, name='utilisateurs'),
    path('creer/', views.creer_view),
]
