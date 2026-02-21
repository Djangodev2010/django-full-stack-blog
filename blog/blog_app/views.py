from django.shortcuts import render, get_object_or_404
from blog_app.models import Category, Blog
from django.http import Http404

# Create your views here.

def home(request):
    # Display all the categories on the homepage and the latest featured posts and regular posts
    categories = Category.objects.all()
    featured_post = Blog.objects.filter(is_featured=True).order_by('-updated_at')
    posts = Blog.objects.filter(is_featured=False, status='Published').order_by('-updated_at')
    return render(request, 'home-blogs.html', context={'categories': categories, 'featured_posts': featured_post, 'posts': posts})

def posts_by_category(request, pk):
    # Fetch the category from the database
    category = Category.objects.get(Category, id=pk)
    categories = Category.objects.all()
    # Fetch the posts that have the same category
    posts = category.blogs.filter(status='Published').order_by('-updated_at')
    return render(request, 'posts_by_category.html', context={'posts': posts, 'categories': categories, 'category': category})
