from django.urls import path
from blog_app import views

app_name = 'blog_app'

urlpatterns = [
    path('', views.home, name='home'),
    path('category/<int:pk>/', views.posts_by_category, name='posts_by_category'),
    path('<slug:slug>/', views.blog_detail, name='blog_detail'),
]

