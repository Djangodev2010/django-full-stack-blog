from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('categories/', views.categories, name='categories'),
    path('categories/add/', views.add_category, name='add-category'),
    path('categories/edit-category/<int:id>/', views.edit_category, name='edit-category'),
    path('categories/delete/<int:id>/', views.delete_category, name='delete-category'),
]

