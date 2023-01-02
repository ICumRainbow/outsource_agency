from django_filters import FilterSet, CharFilter

from post.models import Post


class PostFilter(FilterSet):
    """
    Filter to search posts by name and category.
    """
    heading = CharFilter(lookup_expr='icontains')

    class Meta:
        model = Post
        fields = {
            'heading',
            # 'category',
        }