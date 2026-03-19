from django.shortcuts import render, redirect
from blog_app.models import Blog, Category
from django.contrib.auth.decorators import login_required
from blog_app.forms import CategoryForm, BlogPostForm, AddUserForm, EditUserForm
from django.shortcuts import get_object_or_404
from django.template.defaultfilters import slugify 
from django.contrib.auth.models import User

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

def posts(request):
    posts = Blog.objects.all().order_by('created_at')
    context = {
        'posts': posts,
    }
    return render(request, 'dashboard/posts.html', context=context)

def add_post(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.author = request.user
            form.save()
            title = form.cleaned_data['title']
            form.instance.slug = slugify(title) + '-' + str(form.instance.id)
            form.save()
            return redirect('posts')
        print(form.errors)
    form = BlogPostForm()
    context = {
        'form': form,
    }
    return render(request, 'dashboard/add-post.html', context=context)

def edit_post(request, id):
    post = get_object_or_404(Blog, id=id)
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            title = form.cleaned_data['title']
            form.instance.slug = slugify(title) + '-' + str(form.instance.id)
            form.save()
            return redirect('posts')
        print(form.errors)
    form = BlogPostForm(instance=post)
    context = {
        'form': form
    }
    return render(request, 'dashboard/edit-post.html', context=context)

def delete_post(request, id):
    post = get_object_or_404(Blog, id=id)
    post.delete()
    posts = Blog.objects.all().order_by('created_at')
    context = {
        'posts': posts
    }
    return render(request, 'dashboard/posts.html', context=context)

def users(request):
    users = User.objects.all()
    context = {
        'users': users
    }
    return render(request, 'dashboard/users.html', context=context)

def add_users(request):
    if request.method == 'POST':
        form = AddUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users')
        return redirect('users')
    form = AddUserForm()
    context = {
        'form': form
    }
    return render(request, 'dashboard/add-users.html', context=context)

def edit_user(request, id):
    user = get_object_or_404(User, id=id)
    if request.method == 'POST':
        form = EditUserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('users')
        return redirect('users')
    form = EditUserForm(instance=user)
    context = {
        'form': form
    }
    return render(request, 'dashboard/edit-user.html', context=context)

def delete_user(request, id):
    user = get_object_or_404(User, id=id)
    user.delete()
    return redirect('users')
