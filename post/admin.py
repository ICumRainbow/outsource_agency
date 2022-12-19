from django.contrib import admin
from .models import Post, Category, Tag, Author


# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['heading', 'category', 'get_tags']

    @staticmethod
    def get_tags(obj):
        return ", ".join([p.name for p in obj.tag.all()])


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name', 'occupation']
