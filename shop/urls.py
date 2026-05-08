from django.urls import path
from . import views

urlpatterns = [
    path('', views.site_buketi, name='index'),
    path('product/<int:pk>/', views.detali_buket, name='product'),
]