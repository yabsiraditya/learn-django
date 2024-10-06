from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index),
    path('kontak/', include('kontak.urls')),
    path('admin/', admin.site.urls),
]
