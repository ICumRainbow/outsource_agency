from ckeditor.fields import RichTextField
from django.db import models

from utils.models import BaseModel

from .validators import file_size


class VacancyCategory(BaseModel):
    """
    Model for Vacancy Category, includes name field.
    """
    name = models.CharField(verbose_name='Name', max_length=255)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"VacancyCategory(name='{self.name}')"


class Location(BaseModel):
    """
    Model for Vacancy Location, includes name field.
    """
    name = models.CharField(verbose_name='Location Name', max_length=255)

    class Meta:
        verbose_name_plural = 'Locations'

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"Location(name='{self.name}')"


class Vacancy(BaseModel):
    """
    Model for Vacancy, includes name, category, on site option, remote option, location, content and picture fields.
    """
    name = models.CharField(verbose_name='Name', max_length=255)
    category = models.ForeignKey(verbose_name='Category', to=VacancyCategory, on_delete=models.CASCADE)
    on_site_option = models.BooleanField(verbose_name='On-Site Option', default=False)
    remote_option = models.BooleanField(verbose_name='Remote Option', default=False)
    location = models.ForeignKey(verbose_name='Location', to=Location, on_delete=models.CASCADE)
    content = RichTextField(verbose_name='Content', blank=False, null=False)
    picture = models.ImageField(verbose_name='Picture')

    class Meta:
        verbose_name = 'Vacancy'
        verbose_name_plural = 'Vacancies'

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"Vacancy(name='{self.name}', category='{self.category}')"


class VacancyApplication(models.Model):
    full_name = models.CharField(verbose_name='Full Name', max_length=255, blank=False)
    email = models.EmailField(verbose_name='E-mail', blank=False)
    vacancy = models.ForeignKey(verbose_name='Vacancy', to=Vacancy, on_delete=models.DO_NOTHING)
    resume = models.FileField(verbose_name='Resume', upload_to='uploads/vacancy_resume', validators=[file_size])

    class Meta:
        verbose_name = 'Vacancy application'
        verbose_name_plural = 'Vacancy applications'

    def __str__(self):
        return f"{self.full_name} {self.vacancy.name}"

    def __repr__(self):
        return f"VacancyApplication(vacancy={self.vacancy}, email={self.email})"


class FreelanceApplication(models.Model):
    full_name = models.CharField(verbose_name='Full Name', max_length=255, blank=False)
    email = models.EmailField(verbose_name='E-mail', blank=False)
    resume = models.FileField(verbose_name='Resume', upload_to='uploads/freelance_resume', validators=[file_size])

    class Meta:
        verbose_name = 'Freelance application'
        verbose_name_plural = 'Freelance applications'

    def __str__(self):
        return self.full_name

    def __repr__(self):
        return f"FreelanceApplication(full_name={self.full_name}, email={self.email})"
