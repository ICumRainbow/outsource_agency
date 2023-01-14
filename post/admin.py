from django.contrib import admin
from .models import Post, Category, Tag, Author


# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['heading', 'category', 'get_tags']

    @admin.display(description='Tags', ordering='tag__name')
    def get_tags(self, obj):
        return ", ".join([p.name for p in obj.tag.all()])

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('tag')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name', 'occupation']
