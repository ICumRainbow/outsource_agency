from django.shortcuts import render


# Create your views here.
from our_works.models import Work


def home_view(request):
    works = Work.objects.all()
    context = {
        'works': works
    }
    return render(request, 'home.html', context)
