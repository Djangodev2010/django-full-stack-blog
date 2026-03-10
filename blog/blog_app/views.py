from django.shortcuts import render, get_object_or_404
from blog_app.models import Category, Blog
from django.http import Http404
from django.db.models import Q

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
    similar_blogs = Blog.objects.filter(category=blog.category, status='Published').exclude(id=blog.id)
    return render(request, 'blog_detail.html', context={'blog': blog, 'similar_blogs': similar_blogs})

def blog_search(request):
    keyword = request.GET.get('keyword')
    blogs = Blog.objects.filter(Q(title__icontains=keyword) | Q(short_description__icontains=keyword), status='Published')
    return render(request, 'search.html', context={'blogs': blogs, 'searched_term': keyword})
