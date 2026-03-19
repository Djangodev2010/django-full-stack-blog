from django.urls import path
from . import views

urlpatterns = [
    # Category CRUD
    path('', views.dashboard, name='dashboard'),
    path('categories/', views.categories, name='categories'),
    path('categories/add/', views.add_category, name='add-category'),
    path('categories/edit-category/<int:id>/', views.edit_category, name='edit-category'),
    path('categories/delete/<int:id>/', views.delete_category, name='delete-category'),

    # Posts CRUD
    path('posts/', views.posts, name='posts'),
    path('posts/add-post/', views.add_post, name='add-post'),
    path('posts/edit-post/<int:id>/', views.edit_post, name='edit-post'),
    path('posts/delete-post/<int:id>/', views.delete_post, name='delete-post'),

    # Users CRUD
    path('users/', views.users, name='users'),
    path('users/add-users/', views.add_users, name='add-users'),
    path('users/edit-user/<int:id>/', views.edit_user, name='edit-user'),
    path('users/delete-user/<int:id>/', views.delete_user, name='delete-user')
]

