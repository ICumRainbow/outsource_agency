from asgiref.sync import async_to_sync
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.shortcuts import render, redirect

from contact_bot.utils import send_message
from core.views import for_ctos_view
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
        if form.is_valid():
            # forming a message
            subject = "Website Inquiry"
            body = \
                f"""
                first_name: {form.cleaned_data['first_name']},
                last_name: {form.cleaned_data['last_name']},
                business_email: {form.cleaned_data['business_email']},
                country: {COUNTRY[form.cleaned_data['country']]},
                company: {form.cleaned_data['company']},
                business_title: {form.cleaned_data['business_title']},
                project_details: {form.cleaned_data['project_details']},
                budget: {BUDGET[form.cleaned_data['budget']]},
                needs: {", ".join([NEEDS[i] for i in form.cleaned_data['needs']])}
                """
            print(body)
            # message = "\n".join(map(str, body.values()))
            async_to_sync(send_message)(body)
            try:
                send_mail(subject, body, DEFAULT_FROM_EMAIL, ['to@example.com'], fail_silently=False, )
            except BadHeaderError:
                return HttpResponse('Something went wrong. Please try again.')
            return redirect(for_ctos_view)
    form = MainContactForm()
    context = {
        'form': form,
    }
    return render(request, 'contact.html', context)
