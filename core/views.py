from asgiref.sync import async_to_sync
from django.core.mail import EmailMessage, BadHeaderError
from django.http import HttpResponse
from django.shortcuts import render, redirect

from contact_bot.utils import send_message
from core.services import get_works
from social.forms import SecondaryContactForm


def home_view(request):
    """
    View for Home page.
    """
    works = get_works()
    context = {
        'works': works,
    }
    return render(request, 'index.html', context)


def for_ctos_view(request):
    """
    View for "For CTOs" page that includes secondary contact form with two fields.
    """
    works = get_works()
    if request.method == 'POST':
        form = SecondaryContactForm(request.POST)
        if form.errors:
            print(form.errors.as_text)
        if form.is_valid():
            # forming a message
            subject = "Website Inquiry"
            body = {
                'business_email': form.cleaned_data['business_email'],
                'project_details': form.cleaned_data['project_details'],
            }
            message = "\n".join(map(str, body.values()))
            async_to_sync(send_message)(message)
            try:
                message = EmailMessage(subject, message, 'onetwo20003@gmail.com', ['onetwo20003@gmail.com'])
                eml_content = message.message().as_bytes()
                with open('message.eml', mode='wb') as file:
                    file.write(eml_content)
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect(for_ctos_view)
    form = SecondaryContactForm()
    context = {
        'works': works,
        'form': form,
    }
    return render(request, 'for_ctos.html', context)


def product_innovation_view(request):
    """
    View for Product Innovation page.
    """
    return render(request, 'product_innovation.html')


def services_view(request):
    """
    View for Services page.
    """
    return render(request, 'services.html')


def culture_view(request):
    """
    View for Culture page.
    """
    return render(request, 'сulture.html')
