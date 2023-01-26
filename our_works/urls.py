from django.urls import path
from . import views

urlpatterns = [
    path('works/', views.works_view, name='works'),
    path('work/<int:id_>', views.work_details_view, name='works_details'),
]