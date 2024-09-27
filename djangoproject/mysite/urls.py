from . import views

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', views.index),
    path('blog/', include('blog.urls')),
    path('contact/', include('contact.urls')),
    path('admin/', admin.site.urls),
]
