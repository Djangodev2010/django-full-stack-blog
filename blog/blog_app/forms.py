from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Category, Blog

# For Blog App
class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']


# For Dashboard
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['category_name']

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'short_description', 'blog_body', 'category', 'featured_image', 'is_featured', 'status']

class AddUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2', 'groups', 'user_permissions', 'is_active', 'is_staff', 'is_superuser']

class EditUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'groups', 'user_permissions', 'is_active', 'is_staff', 'is_superuser']
