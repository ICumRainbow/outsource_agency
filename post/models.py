from ckeditor.fields import RichTextField
from django.db import models

from core.models import BaseModel


class Category(BaseModel):
    """
    Model for Categories, includes name and description fields.
    """
    name = models.CharField(verbose_name='Category', max_length=255)
    description = models.TextField(verbose_name='Description', blank=True, null=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"Category(name='{self.name}')"


class Tag(BaseModel):
    """
    Model for Tags, includes name field.
    """
    name = models.CharField(verbose_name='Tag', max_length=255)

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"<Tag {self.name}>"


class Author(BaseModel):
    """
    Model for Authors, includes name, avatar, occupation and about fields.
    """
    name = models.CharField(verbose_name='Author', max_length=255)
    avatar = models.ImageField(verbose_name='Avatar', blank=False, default='blank_avatar.jpg')
    occupation = models.CharField(verbose_name='Occupation', max_length=255)
    about = models.TextField(verbose_name='About', max_length=500)

    class Meta:
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"<Author {self.name}>"


class Post(BaseModel):
    """
    Model for Posts, includes picture, heading, content, category, tag, author and time to read fields.
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

    def __repr__(self):
        return f"<Post {self.heading}>"
