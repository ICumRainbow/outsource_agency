from asgiref.sync import async_to_sync
from contact_bot.utils import send_message
from core.views import home_view
from django.contrib import messages
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.shortcuts import render, redirect
from outsource.settings import DEFAULT_FROM_EMAIL
from social.constants import BUDGET, COUNTRY, NEEDS
from social.forms import MainContactForm


def contact_view(request):
    """
    View for Contact Us page that includes the main contact form.
    """
    if request.method == 'POST':
        form = MainContactForm(request.POST)
        if form.errors:
            print(form.errors.as_text)
            messages.success(request, 'Something went wrong, please try again!')
        if form.is_valid():
            form.save()

            # forming a message
            subject = "Website Inquiry"

            body = \
                (f"First name: {form.cleaned_data['first_name']}\n"
                 f"Last name: {form.cleaned_data['last_name']}\n"
                 f"Email: {form.cleaned_data['business_email']}\n"
                 f"Country: {COUNTRY[form.cleaned_data['country']]}\n"
                 f"Company: {form.cleaned_data['company']}\n"
                 f"Business title: {form.cleaned_data['business_title']}\n"
                 f"Project details: {form.cleaned_data['project_details']}\n"
                 f"Budget: {BUDGET[form.cleaned_data['budget']]}\n"
                 f"Needs: {', '.join([NEEDS[i] for i in form.cleaned_data['needs']])}"
                 )
            async_to_sync(send_message)(body)
            messages.success(request, 'Thank you for your message! We will answer you soon!')
            try:
                send_mail(subject, body, DEFAULT_FROM_EMAIL, ['to@example.com'], fail_silently=False)
            except BadHeaderError:
                return HttpResponse('Something went wrong. Please try again.')
            return redirect(home_view)
    form = MainContactForm()
    context = {
        'form': form,
    }
    return render(request, 'contact.html', context)
