from django.urls import path

from . import views

urlpatterns = [
    path('blog/', views.blog_view, name='blog'),
    path('post/<int:id_>', views.post_view, name='post')
]