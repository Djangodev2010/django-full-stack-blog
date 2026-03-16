from django.shortcuts import render, redirect
from blog_app.models import Blog, Category
from django.contrib.auth.decorators import login_required
from blog_app.forms import CategoryForm
from django.shortcuts import get_object_or_404 

# Create your views here.

@login_required(login_url='blog_app:login')
def dashboard(request):
    blogs_count = Blog.objects.all().count()
    category_count = Category.objects.all().count()
    
    context = {
        'blog_count': blogs_count,
        'category_count': category_count
    }
    return render(request, 'dashboard/dashboard.html', context=context)

def categories(request):
    return render(request, 'dashboard/categories.html')

def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categories')
    form = CategoryForm()
    context = {
        'form': form
    }
    return render(request, 'dashboard/add-category.html', context=context)

def edit_category(request, id):
    category = get_object_or_404(Category, id=id)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('categories')
    form = CategoryForm(instance=category)
    context = {
        'form': form,
        'category': category
    }
    return render(request, 'dashboard/edit-category.html', context=context)

def delete_category(request, id):
    category = get_object_or_404(Category, id=id)
    category.delete()
    return redirect('categories')
