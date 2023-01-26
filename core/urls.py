from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('for-ctos/', views.for_ctos_view, name='for_CTOs'),
    path('product-innovation/', views.product_innovation_view, name='product-innovation'),
    path('services/', views.services_view, name='services'),
    path('culture/', views.culture_view, name='culture'),
]