import os
import asyncio

import django
from asgiref.sync import sync_to_async, async_to_sync
from django.core.mail import send_mail, BadHeaderError, EmailMessage
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from contact_bot.utils import send_message
from core.views import for_CTOs_view
from outsource.settings import DEFAULT_FROM_EMAIL
from social.forms import MainContactForm


def contact_view(request):
    """
    View for Contact Us page that includes the main contact form.
    """
    if request.method == 'POST':
        form = MainContactForm(request.POST)
        if form.errors:
            print(form.errors.as_text)
        if form.is_valid():
            # forming a message
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
            message = "\n".join(map(str, body.values()))
            async_to_sync(send_message)(message)
            try:
                send_mail(subject, message, DEFAULT_FROM_EMAIL, ['to@example.com'], fail_silently=False,)
            except BadHeaderError:
                return HttpResponse('Something went wrong. Please try again.')
            return redirect(for_CTOs_view)
    form = MainContactForm()
    context = {
        'form': form,
    }
    return render(request, 'contact.html', context)
