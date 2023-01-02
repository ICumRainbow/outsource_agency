from django.urls import path
from . import views

urlpatterns = [
    path('', views.for_CTOs_view, name='for_CTOs'),
    path('product-innovation/', views.product_innovation_view, name='product-innovation'),
]