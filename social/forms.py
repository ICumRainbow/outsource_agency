from django import forms


# Create your forms here.
from social.constants import COUNTRY_CHOICES, BUDGET_CHOICES, NEEDS_CHOICES


class MainContactForm(forms.Form):
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


class SecondaryContactForm(forms.Form):
    business_email = forms.EmailField(
        widget=forms.TextInput(attrs={'class': 'input', 'id': 'email', 'placeholder': 'Email Address'}))
    project_details = forms.CharField(widget=forms.Textarea, max_length=2000, required=False)
