from django.urls import path

# import views
from . import views


app_name = 'pulangpergi'
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.addDestination , name='create'),
    path('delete/<slug:nameSlug>/', views.delete, name='delete'),
    path('update/<slug:nameSlug>/', views.update, name='update'),
]
