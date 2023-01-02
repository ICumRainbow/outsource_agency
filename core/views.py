from django.core.mail import EmailMessage, BadHeaderError
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from contact_bot.utils import send_message
from our_works.models import Work
from social.forms import SecondaryContactForm


def for_CTOs_view(request):
    """
    View for "For CTOs" page that includes secondary contact form with two fields.
    """
    works = Work.objects.all()
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
            send_message(message)
            try:
                message = EmailMessage(subject, message, 'onetwo20003@gmail.com', ['onetwo20003@gmail.com'])
                eml_content = message.message().as_bytes()
                with open('message.eml', mode='wb') as file:
                    file.write(eml_content)
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect(for_CTOs_view)
    form = SecondaryContactForm()
    context = {
        'works': works,
        'form': form,
    }
    return render(request, 'home.html', context)


def product_innovation_view(request):
    return render(request, 'product_innovation.html')
