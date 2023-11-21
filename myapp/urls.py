from django.urls import path
from . import views

urlpatterns = [
    path('', views.links, name='links'),
    path('index/', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('product_reader/', views.product_reader, name='product_reader'),
    path('client_reader/', views.client_reader, name='client_reader'),
    path('order_reader/', views.order_reader, name='order_reader')
]
