from our_works.models import Work


def get_works() -> Work:
    """
    Returns all Work objects.
    """
    works = Work.objects.all()
    return works
