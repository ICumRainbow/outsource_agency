from django import forms


# Create your forms here.

class MainContactForm(forms.Form):
    BUDGET_CHOICES = (
        ('1', '$50,000 and under'),
        ('2', '$50,000-$200,000'),
        ('3', '$200,000-$1,000,000'),
        ('4', '$1,000,000+')
    )
    COUNTRY_CHOICES = (
        ('1', 'Afghanistan'),
    )
    NEEDS_CHOICES = (
        ('1', 'Strategy'),
        ('2', 'UX & UI Design'),
        ('3', 'Development'),
        ('4', 'Product Scaling'),
        ('5', 'Team Scaling'),
        ('6', 'Strategic Support'),
        ('7', 'Product Innovation'),
        ('8', 'Other'),
    )
    first_name = forms.CharField(max_length=50, required=False)
    last_name = forms.CharField(max_length=50, required=False)
    business_email = forms.EmailField(max_length=150, required=False)
    country = forms.ChoiceField(choices=COUNTRY_CHOICES, required=False)
    company = forms.CharField(max_length=50, required=False)
    business_title = forms.CharField(max_length=50, required=False)
    project_details = forms.CharField(widget=forms.Textarea, max_length=2000, required=False)
    budget = forms.ChoiceField(choices=BUDGET_CHOICES, required=False, widget=forms.Select)
    needs = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=NEEDS_CHOICES, required=False)
