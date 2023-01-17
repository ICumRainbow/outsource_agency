from django import forms
from django_filters import FilterSet, CharFilter, ChoiceFilter, ModelChoiceFilter

from core.models import Vacancy, VacancyCategory, Location


class VacancyFilter(FilterSet):
    """
    Filter to search posts by name and category.
    """
    location = ModelChoiceFilter(queryset=Location.objects.all(), widget=forms.Select(attrs={'class': 'dropdown'}))
    category = ModelChoiceFilter(queryset=VacancyCategory.objects.all(), widget=forms.Select(attrs={'class': 'dropdown'}))

    class Meta:
        model = Vacancy
        fields = [
            'location',
            'category',
        ]
