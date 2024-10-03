from django.urls import path

from . import views

# app_name = Blog
urlpatterns = [
    path('', views.index),
    path('stoping/', views.stoping),
    path('peduli/', views.peduli),
    path('viral/', views.viral),
    path('berita/', views.berita),
]
