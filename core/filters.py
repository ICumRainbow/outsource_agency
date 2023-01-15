from django_filters import FilterSet, CharFilter

from core.models import Vacancy


class VacancyFilter(FilterSet):
    """
    Filter to search posts by name and category.
    """
    location = CharFilter(lookup_expr='exact')
    category = CharFilter(lookup_expr='exact')

    class Meta:
        model = Vacancy
        fields = [
            'location',
            'category',
        ]
