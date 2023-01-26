from django.shortcuts import render

from careers.services import get_careers_page_contents, get_vacancy


def careers_view(request):
    """
    View for Careers page with possible filtering via query parameters.
    """
    query_params = {}
    location = request.GET.get('location', False)
    category = request.GET.get('category', False)
    if location:
        query_params['location_id'] = int(location)
    if category:
        query_params['category_id'] = int(category)
    categories, vacancies = get_careers_page_contents(request.GET, query_params)
    context = {
        'vacancies': vacancies,
        'categories': categories,
    }
    return render(request, 'careers.html', context)


def careers_details_view(request, id_):
    """
    View for details page of available vacancies.
    """
    vacancy = get_vacancy(id_)
    context = {
        'vacancy': vacancy,
    }
    return render(request, 'careers_details.html', context)


def freelance_view(request):
    return render(request, 'freelance.html')
