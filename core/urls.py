from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('posts/', views.post_list, name='post_list'),
    path('posts/<int:pk>/', views.post_detail, name='post_detail'),
    path('posts/add/', views.post_create, name='post_create'),
    path('posts/<int:pk>/edit/', views.post_update, name='post_update'),
    path('posts/<int:pk>/delete/', views.post_delete, name='post_delete'),
    path('profile/', views.profile_detail, name='profile_detail'),
    ]