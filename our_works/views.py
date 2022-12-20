from django.shortcuts import render

# Create your views here.
from our_works.models import Work


def works_view(request):
    """
    View for Works page.
    """
    return render(request, 'works.html')


def work_details_view(request, id_):
    """
    View for details pages of portfolio works.
    """
    work = Work.objects.get(id=id_)
    context = {
        'work': work
    }
    return render(request, 'work.html', context)
