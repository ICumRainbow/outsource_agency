from django.db.models import QuerySet
from django.shortcuts import get_object_or_404

from our_works.models import Work


def get_work_and_next_in_line(id_: int) -> tuple[Work, Work]:
    """
    Accepts id_ as parameter, returns work with this id and next work (or if this work is the latest, the first work).
    :param id_:
    """
    work = get_object_or_404(Work, id=id_)
    next_work = Work.objects.filter(id__gt=id_)

    if next_work:
        next_in_line = next_work[0]
    else:
        first_work = Work.objects.exclude(id=id_).first()
        next_in_line = first_work

    return work, next_in_line


def get_works() -> QuerySet:
    """
    Returns all works from the Work model.
    """
    works = Work.objects.all()

    return works
