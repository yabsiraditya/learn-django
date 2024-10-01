from django.urls import path

from . import views

# App Name = Blog
urlpatterns = [
    path('', views.index)
]
