from django.core.validators import FileExtensionValidator
from django.db import models

from core.models import BaseModel

from .constants import COUNTRY, BUDGET, NEEDS


class Social(BaseModel):
    """
    Model for Social Networks.
    """
    class Meta:
        verbose_name = 'Social'
        verbose_name_plural = 'Socials'

    name = models.CharField(max_length=255)
    logo = models.FileField(verbose_name='Logo', validators=[FileExtensionValidator(['pdf', 'doc', 'svg'])])
    link = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"<Social {self.name}>"


class MainFormRequest(BaseModel):
    """
    Model for contact form requests on the website.
    """
    class Meta:
        verbose_name = 'Main Form Request'
        verbose_name_plural = 'Main Form Requests'

    first_name = models.CharField(verbose_name='First name', max_length=255)
    last_name = models.CharField(verbose_name='Last name', max_length=255)
    business_email = models.EmailField(verbose_name='Business email')
    country = models.CharField(verbose_name='Country', max_length=255)
    company = models.CharField(verbose_name='Company', max_length=255)
    business_title = models.CharField(verbose_name='Business title', max_length=255)
    project_details = models.TextField(verbose_name='Project details')
    budget = models.CharField(verbose_name='Budget', max_length=255)
    needs = models.CharField(verbose_name='Needs', max_length=255, blank=True)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if self._state.adding:
            self.country = COUNTRY[self.country]
            self.budget = BUDGET[self.budget]
            if self.needs:
                self.needs = ", ".join([NEEDS[i] for i in eval(self.needs)])
        super().save(force_insert, force_update, using, update_fields)

    def __str__(self):
        return self.company

    def __repr__(self):
        return f"<Request from {self.company}>"


class SecondaryFormRequest(BaseModel):
    """
    Model for contact form requests on the website.
    """
    class Meta:
        verbose_name = 'Secondary Form Request'
        verbose_name_plural = 'Secondary Form Requests'
    business_email = models.EmailField(verbose_name='Business email')
    project_details = models.TextField(verbose_name='Project details')

    def __str__(self):
        return self.business_email

    def __repr__(self):
        return f"<Request from {self.business_email}>"
