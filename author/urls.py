from django.urls import path

from . import views


app_name = 'author'

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add, name='add'),
    path('<int:pk>/', views.detail, name='detail'),
]