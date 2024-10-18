from django.contrib import admin
from django.urls import path, include

# import views
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('pulangpergi/', include('pulangpergi.urls', namespace='pulangpergi')),
    path('admin/', admin.site.urls),
]
