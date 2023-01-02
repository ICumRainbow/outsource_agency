from post.filters import PostFilter
from post.models import Category, Post


def get_blog_page_contents(request_dict: dict = None, query_params: dict = None):
    """
    Getting all the contents for the Blog page.
    """
    categories = Category.objects.all()
    posts_by_date = Post.objects.order_by('-created_at')
    posts = None
    if query_params:
        posts = posts_by_date.filter(**query_params)
        posts = PostFilter(request_dict, queryset=posts)
    return categories, posts_by_date, posts
