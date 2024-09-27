from django.urls import path

from . import views 

# app_name = blog
urlpatterns = [
    path('', views.index),
    path('artikel/', views.artikel),
    path('berita/', views.berita),
]
