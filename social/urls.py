from django.urls import path, include
from . import views

urlpatterns = [
    path('contact/', views.contact_view, name='contact'),
    path('', include('core.urls')),
]