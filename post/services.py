from django.shortcuts import get_object_or_404

from post.filters import PostFilter
from post.models import Category, Post


def get_blog_page_contents(request_dict: dict = None, query_params: dict = None) -> [Category, Post, Post, Post]:
    """
    Getting all the contents for the Blog page.
    """
    categories = Category.objects.all()
    headliner = Post.objects.first()
    posts_by_date = Post.objects.order_by('-created_at')
    posts = None
    if query_params:
        posts = posts_by_date.filter(**query_params)
        posts = PostFilter(request_dict, queryset=posts)
    return categories, headliner, posts_by_date, posts


def get_post_and_related_posts(id_: int) -> [Post, Post]:
    """
    Getting post and related posts with the same category id.
    """
    post = get_object_or_404(Post, id=id_)
    related_posts = Post.objects.filter(category=id_).exclude(id=id_)[:2]
    return post, related_posts
