from django.shortcuts import render, get_object_or_404
from blog_app.models import Category, Blog, Comment
from django.http import Http404
from django.db.models import Q
from .forms import UserRegistrationForm
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth

# Create your views here.

def home(request):
    # Display all the categories on the homepage and the latest featured posts and regular posts
    featured_post = Blog.objects.filter(is_featured=True).order_by('-updated_at')
    posts = Blog.objects.filter(is_featured=False, status='Published').order_by('-updated_at')
    return render(request, 'home-blogs.html', context={'featured_posts': featured_post, 'posts': posts})

def posts_by_category(request, pk):
    # Fetch the category from the database
    category = get_object_or_404(Category, id=pk)
    # Fetch the posts that have the same category
    posts = category.blogs.filter(status='Published').order_by('-updated_at')
    return render(request, 'posts_by_category.html', context={'posts': posts, 'category': category})

def blog_detail(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    comments = Comment.objects.filter(blog=blog)
    comment_count = Comment.objects.filter(blog=blog).count()
    similar_blogs = Blog.objects.filter(category=blog.category, status='Published').exclude(id=blog.id)
    return render(request, 'blog_detail.html', context={'blog': blog, 'similar_blogs': similar_blogs, 'comments': comments, 'comment_count': comment_count})

def blog_search(request):
    keyword = request.GET.get('keyword')
    blogs = Blog.objects.filter(Q(title__icontains=keyword) | Q(short_description__icontains=keyword), status='Published')
    return render(request, 'search.html', context={'blogs': blogs, 'searched_term': keyword})

def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("blog_app:login")
    else:
        form = UserRegistrationForm()
    return render(request, "register.html", {"form": form})

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('blog_app:home')
            return redirect('blog_app:login')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', context={'form': form})

def logout(request):
    auth.logout(request)
    return redirect('blog_app:home')

def add_comment(request, id):
    if request.method == 'POST':
        comment_body = request.POST.get('body')
        user = request.user
        blog = get_object_or_404(Blog, id=id)
        comment = Comment.objects.create(blog=blog, body=comment_body, user=user)
        comment.save()
        comments = Comment.objects.filter(blog=blog)
        similar_blogs = Blog.objects.filter(category=blog.category)
        context = {
            'blog': blog,
            'comments': comments,
            'similar_blogs': similar_blogs
        }
        return redirect('blog_app:blog_detail', slug=blog.slug)
    return render(request, 'blog_detail.html', context=context)
