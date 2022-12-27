from django.core.mail import send_mail, BadHeaderError, EmailMessage
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from contact_bot.utils import send_message
from core.views import home_view
from social.forms import MainContactForm


def contact_view(request):
    if request.method == 'POST':
        form = MainContactForm(request.POST)
        if form.errors:
            print(form.errors.as_text)
        if form.is_valid():
            subject = "Website Inquiry"
            body = {
                'first_name': form.cleaned_data['first_name'],
                'last_name': form.cleaned_data['last_name'],
                'business_email': form.cleaned_data['business_email'],
                'country': form.cleaned_data['country'],
                'company': form.cleaned_data['company'],
                'business_title': form.cleaned_data['business_title'],
                'project_details': form.cleaned_data['project_details'],
                'budget': form.cleaned_data['budget'],
                'needs': form.cleaned_data['needs'],
            }
            print(form.cleaned_data['country'], form.cleaned_data['budget'])
            message = "\n".join(map(str, body.values()))
            send_message(message)
            try:
                message = EmailMessage(subject, message, 'onetwo20003@gmail.com', ['onetwo20003@gmail.com'])
                eml_content = message.message().as_bytes()
                print(eml_content)
                with open('message.eml', mode='wb') as file:
                    file.write(eml_content)
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect(home_view)
    form = MainContactForm()
    context = {
        'form': form,
    }
    return render(request, 'contact.html', context)
