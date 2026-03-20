from django.urls import path
from blog_app import views

app_name = 'blog_app'

urlpatterns = [
    # Homepage
    path('', views.home, name='home'),

    # Sorted posts by category
    path('category/<int:pk>/', views.posts_by_category, name='posts_by_category'),

    # Search endpoint
    path('search/', views.blog_search, name='search'),

    # Blog details
    path('blogs/<slug:slug>/', views.blog_detail, name='blog_detail'),

    # Registeration
    path('register', views.register, name='register'),

    # Login 
    path('login', views.login, name='login'),

    # Logout
    path('logout', views.logout, name='logout'),

    # Adding Comments endpoint
    path('add-comment/<int:id>/', views.add_comment, name='add-comment'),

]

