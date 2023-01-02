from social.models import Social


def get_socials(request):
    socials = Social.objects.all()
    context = {
        'socials': socials
    }
    return context
