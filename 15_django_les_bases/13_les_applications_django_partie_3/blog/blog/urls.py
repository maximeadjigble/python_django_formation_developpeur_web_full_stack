from django.contrib import admin
from django.urls import path, include

from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_view, name='home'),
    path('contact/', views.contact_view, name='contact'),
    path('articles/', views.articles_view, name='articles'),
    path('utilisateurs/', include('utilisateurs.urls')),
]
