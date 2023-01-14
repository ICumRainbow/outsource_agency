from django.core.paginator import Paginator
from django.shortcuts import render

# Create your views here.
from post.services import get_blog_page_contents


def blog_view(request):
    """
    View for blog page.
    """
    post_heading = request.GET.get('heading', '')
    category = request.GET.get('category', False)
    # setting query kwargs depending on the GET request
    query_params = {'heading__icontains': post_heading}
    if category:
        query_params['category_id'] = int(category)
    categories, headliner, posts_by_date, posts = get_blog_page_contents(request.GET, query_params)
    paginator = Paginator(posts.qs, 10)
    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)
    page_range = paginator.get_elided_page_range(number=page.number, on_each_side=3, on_ends=2)
    context = {
        'categories': categories,
        'posts_by_date': posts_by_date[:6],
        'page': page,
        'posts': posts,
        'headliner': headliner,
        'page_range': page_range
    }
    return render(request, 'blog.html', context)
