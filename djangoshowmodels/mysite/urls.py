from django.contrib import admin
from django.urls import path, include

from .views import index

urlpatterns = [
    path('', index),
    path('blog/', include('blog.urls')),
    path('admin/', admin.site.urls),
]