from datetime import datetime

from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.
from core.models import BaseModel


class Category(BaseModel):
    """
    Model for Categories.
    """
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Tag(BaseModel):
    """
    Model for Tags.
    """
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'

    def __str__(self):
        return self.name


class Author(BaseModel):
    """
    Model for Authors.
    """
    name = models.CharField(max_length=255)
    avatar = models.ImageField(blank=False, default='blank_avatar.jpg')
    occupation = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'

    def __str__(self):
        return self.name


class Post(BaseModel):
    """
    Model for Posts.
    """
    picture = models.ImageField(verbose_name='Picture')
    heading = models.CharField(verbose_name='Heading', max_length=255)
    content = RichTextField(verbose_name='Content', blank=False, null=False)
    category = models.ForeignKey(verbose_name='Category', to=Category, on_delete=models.CASCADE)
    tag = models.ManyToManyField(verbose_name='Tag', to=Tag, blank=True)
    author = models.ForeignKey(verbose_name='Author', to=Author, on_delete=models.CASCADE, default=1)
    time_to_read = models.CharField(verbose_name='Time to read', blank=True, max_length=255)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return self.heading

