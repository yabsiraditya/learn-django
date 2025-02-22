from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    # path('changepassword/', views.change_password_user, name='changepassword'),
    path('changepassword1/', views.change_password, name='changepassword1'),
    path('admin/', admin.site.urls),
]
