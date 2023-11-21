from django.urls import path
from . import views

urlpatterns = [
    path('', views.links, name='links'),
    path('product_reader/', views.product_reader, name='product_reader'),
    path('client_reader/', views.client_reader, name='client_reader'),
    path('order_reader/', views.order_reader, name='order_reader'),
    path('add_client/', views.add_client, name='add_client'),
    path('add_product/', views.add_product, name='add_product'),
]
