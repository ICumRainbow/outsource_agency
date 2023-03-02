from django import forms

from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV3
from careers.models import VacancyApplication, FreelanceApplication
from outsource import settings


class VacancyApplicationForm(forms.ModelForm):
    """
    Vacancy application form with captcha field.
    """

    class Meta:
        model = VacancyApplication
        fields = ['full_name', 'email', 'resume']

    full_name = forms.CharField(widget=forms.TextInput(attrs={'type': 'text', 'id': 'name', 'placeholder': 'Full name'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'id': 'email', 'placeholder': 'E-mail'}))
    resume = forms.FileField(widget=forms.FileInput(attrs={'type': 'file', 'id': 'CV'}))
    captcha = ReCaptchaField(
        public_key=settings.RECAPTCHA_PUBLIC_KEY,
        private_key=settings.RECAPTCHA_PRIVATE_KEY,
        widget=ReCaptchaV3
    )


class FreelanceApplicationForm(forms.ModelForm):
    """
    Freelance application form with captcha field.
    """

    class Meta:
        model = FreelanceApplication
        fields = ['full_name', 'email', 'resume']

    full_name = forms.CharField(widget=forms.TextInput(attrs={'type': 'text', 'id': 'name', 'placeholder': 'Full name'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'id': 'email', 'placeholder': 'E-mail'}))
    resume = forms.FileField(widget=forms.FileInput(attrs={'type': 'file', 'id': 'CV'}))
    captcha = ReCaptchaField(
        public_key=settings.RECAPTCHA_PUBLIC_KEY,
        private_key=settings.RECAPTCHA_PRIVATE_KEY,
        widget=ReCaptchaV3
    )
