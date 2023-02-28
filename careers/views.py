from django.contrib import messages
from django.core.mail import BadHeaderError, send_mail, EmailMessage
from django.http import HttpResponse
from django.shortcuts import render
from contact_bot.utils import send_file
from asgiref.sync import async_to_sync

from careers.services import get_careers_page_contents, get_vacancy

from careers.forms import VacancyApplicationForm, FreelanceApplicationForm

from outsource.settings import DEFAULT_FROM_EMAIL


def careers_view(request):
    """
    View for Careers page with possible filtering via query parameters.
    """
    query_params = {}
    location = request.GET.get('location', False)
    category = request.GET.get('category', False)
    if location:
        query_params['location_id'] = int(location)
    if category:
        query_params['category_id'] = int(category)
    categories, vacancies = get_careers_page_contents(request.GET, query_params)
    context = {
        'vacancies': vacancies,
        'categories': categories,
    }
    return render(request, 'careers.html', context)


def careers_details_view(request, id_):
    """
    View for details page of available vacancies.
    """
    vacancy = get_vacancy(id_)
    form = VacancyApplicationForm()
    if request.method == 'POST':
        form = VacancyApplicationForm(request.POST, request.FILES)
        resume = request.FILES['resume']
        if form.errors:
            print(form.errors)
        if form.is_valid():
            application_form = form.save(commit=False)
            application_form.resume = resume
            application_form.vacancy = vacancy
            application_form.save()
            # forming a message
            subject = "Website Inquiry"
            body = \
                (
                    f"Name: {form.cleaned_data['full_name']}\n"
                    f"Email: {form.cleaned_data['email']}\n"
                    f"Vacancy: {vacancy.name}\n"
                )
            resume_path = application_form.resume.path
            async_to_sync(send_file)(resume_path, body)
            messages.success(request, 'Thank you for your message! We will answer you soon!')
            try:
                mail = EmailMessage(subject, body, DEFAULT_FROM_EMAIL, ['to@example.com'])
                mail.attach(resume.name, resume.read(), resume.content_type)
                mail.send(fail_silently=False)
            except BadHeaderError:
                return HttpResponse('Something went wrong. Please try again.')
        else:
            messages.error(request, 'Something went wrong. Please try again.')

    context = {
        'vacancy': vacancy,
        'form': form,
    }
    return render(request, 'careers_details.html', context)


def freelance_view(request):
    form = FreelanceApplicationForm()
    if request.method == 'POST':
        form = FreelanceApplicationForm(request.POST, request.FILES)
        resume = request.FILES['resume']
        if form.errors:
            print(form.errors)
        if form.is_valid():
            application_form = form.save(commit=False)
            application_form.resume = resume
            application_form.save()
            # forming a message
            subject = "Website Inquiry"
            body = \
                (
                    f"Name: {form.cleaned_data['full_name']}\n"
                    f"Email: {form.cleaned_data['email']}\n"
                )
            resume_path = application_form.resume.path
            async_to_sync(send_file)(resume_path, body)
            messages.success(request, 'Thank you for your message! We will answer you soon!')
            try:
                mail = EmailMessage(subject, body, DEFAULT_FROM_EMAIL, ['to@example.com'])
                mail.attach(resume.name, resume.read(), resume.content_type)
                mail.send(fail_silently=False)
            except BadHeaderError:
                return HttpResponse('Something went wrong. Please try again.')
        else:
            messages.error(request, 'Something went wrong. Please try again.')

    context = {
        'form': form,
    }
    return render(request, 'freelance.html', context)
