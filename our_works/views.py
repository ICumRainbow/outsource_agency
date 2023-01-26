from django.shortcuts import render

from our_works.services import get_work_and_next_in_line, get_works


def works_view(request):
    """
    View for Works page.
    """
    works = get_works()
    context = {
        'works': works,
    }
    return render(request, 'works.html', context)


def work_details_view(request, id_: int):
    """
    View for details page of portfolio works.
    """
    work, next_in_line = get_work_and_next_in_line(id_)
    context = {
        'work': work,
        'next_in_line': next_in_line,
    }
    return render(request, 'work.html', context)
