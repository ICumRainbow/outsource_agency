import os

from django import forms

from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV3
from social.constants import COUNTRY_CHOICES, BUDGET_CHOICES, NEEDS_CHOICES

from .models import MainFormRequest, SecondaryFormRequest
from outsource import settings


class MainContactForm(forms.ModelForm):
    """
    Main contact form with captcha field.
    """
    class Meta:
        model = MainFormRequest
        fields = ['first_name', 'last_name', 'business_email', 'country', 'company', 'business_title',
                  'project_details', 'budget', 'needs']

    first_name = forms.CharField(max_length=50, required=False,
                                 widget=forms.TextInput(attrs={'class': 'form-input', 'id': 'name'}))
    last_name = forms.CharField(max_length=50, required=False,
                                widget=forms.TextInput(attrs={'class': 'form-input', 'id': 'last-name'}))
    business_email = forms.EmailField(max_length=150, required=False,
                                      widget=forms.TextInput(attrs={'class': 'form-input', 'id': 'email'}))
    country = forms.ChoiceField(choices=COUNTRY_CHOICES, required=False,
                                widget=forms.Select(attrs={'class': 'dropdown'}))
    company = forms.CharField(max_length=50, required=False,
                              widget=forms.TextInput(attrs={'class': 'form-input', 'id': 'company-name'}))
    business_title = forms.CharField(max_length=50, required=False,
                                     widget=forms.TextInput(attrs={'class': 'form-input', 'id': 'title'}))
    project_details = forms.CharField(max_length=2000, required=False,
                                      widget=forms.Textarea(attrs={'class': 'form-input-wide', 'id': 'info'}))
    budget = forms.ChoiceField(choices=BUDGET_CHOICES, required=False, widget=forms.Select(attrs={'class': 'dropdown'}))
    needs = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=NEEDS_CHOICES, required=False)

    captcha = ReCaptchaField(
        public_key=settings.RECAPTCHA_PUBLIC_KEY,
        private_key=settings.RECAPTCHA_PRIVATE_KEY,
        widget=ReCaptchaV3
    )


class SecondaryContactForm(forms.ModelForm):
    """
    Secondary contact form with captcha field.
    """
    class Meta:
        model = SecondaryFormRequest
        fields = ['business_email', 'project_details']

    business_email = forms.EmailField(
        widget=forms.TextInput(attrs={'class': 'input', 'id': 'email', 'placeholder': 'Email Address'}))
    project_details = forms.CharField(widget=forms.Textarea(attrs={'id': 'text'}), max_length=2000, required=False)
    captcha = ReCaptchaField(
        public_key=settings.RECAPTCHA_PUBLIC_KEY,
        private_key=settings.RECAPTCHA_PRIVATE_KEY,
        widget=ReCaptchaV3
    )
