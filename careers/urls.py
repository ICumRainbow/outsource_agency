from django.urls import path
from . import views

urlpatterns = [
    path('careers/', views.careers_view, name='careers'),
    path('careers-details/<int:id_>', views.careers_details_view, name='careers_details'),
    path('freelance/', views.freelance_view, name='freelance'),
]