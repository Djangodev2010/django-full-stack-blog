from django.db import models
from django.contrib.auth.models import User

# Create your models here.

STATUS = [
    ("Draft", "Draft"),
    ("Published", "Published")
]

class Category(models.Model):
    category_name = models.CharField(max_length=50, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.category_name

class Blog(models.Model):
    title = models.CharField(max_length=155)
    slug = models.SlugField(max_length=155, unique=True, blank=True)
    short_description = models.CharField(max_length=355)
    blog_body = models.TextField(max_length=2000)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='blogs')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(choices=STATUS, default="Draft")
    is_featured = models.BooleanField(default=False)
    featured_image = models.ImageField(upload_to='uploads/%Y/%m/%d')

    class Meta:
        verbose_name_plural = 'Blogs'

    def __str__(self):
        return self.title
