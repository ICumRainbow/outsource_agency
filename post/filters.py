from django import forms
from django.db.models import Q
from django_filters import FilterSet, CharFilter

from post.models import Post


class PostFilter(FilterSet):
    """
    Filter to search posts by name and category.
    """
    heading_and_tag = CharFilter(method='heading_and_tag_filter', lookup_expr='icontains',
                                 widget=forms.TextInput(attrs={'id': 'id_heading', 'type': 'search', 'class': 'nav-search'}))

    class Meta:
        model = Post
        fields = [
            'heading_and_tag',
            # 'category',
        ]

    def heading_and_tag_filter(self, queryset, name, value):
        return queryset.filter(
            Q(heading__icontains=value) | Q(tag__name__icontains=value)
        )
