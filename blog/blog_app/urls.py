from django.urls import path
from blog_app import views

urlpatterns = [
    path('', views.home, name='home'),
    path('category/<int:pk>/', views.posts_by_category, name='posts_by_category'),
]

