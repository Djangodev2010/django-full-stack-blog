from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Category

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class LoginForm():
    pass

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['category_name']
