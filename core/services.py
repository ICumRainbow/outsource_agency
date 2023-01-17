from core.filters import VacancyFilter
from core.models import Vacancy, VacancyCategory


def get_careers_page_contents(request_dict: dict = None, query_params: dict = None):
    """
    Getting all the contents for the Careers page.
    """
    categories = VacancyCategory.objects.all()
    vacancies_by_date = Vacancy.objects.order_by('-created_at')
    # vacancies = None
    # if query_params:
    vacancies = vacancies_by_date.filter(**query_params)
    vacancies = VacancyFilter(request_dict, queryset=vacancies)
    return categories, vacancies
