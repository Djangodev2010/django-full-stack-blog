from django.contrib import admin
from blog_app.models import Category, Blog, SocialLinks

# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'author', 'is_featured', 'category', 'status')
    search_fields = ('id', 'title', 'category__category_name', 'status')
    list_editable = ('status', 'is_featured',)

admin.site.register(Category)
admin.site.register(Blog, BlogAdmin)
admin.site.register(SocialLinks)
