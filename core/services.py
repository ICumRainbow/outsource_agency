from our_works.models import Work


def get_works() -> Work:
    """
    Returns all Work objects.
    """
    works = Work.objects.all()
    if len(works) > 2:
        works = works[:2]
    return works
