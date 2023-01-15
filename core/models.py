from datetime import datetime

from ckeditor.fields import RichTextField
from django.db import models


# Create your models here.

class BaseModel(models.Model):
    created_at = models.DateTimeField(verbose_name='Created at', default=datetime.now)

    class Meta:
        abstract = True


class VacancyCategory(BaseModel):
    name = models.CharField(verbose_name='Name', max_length=255)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Location(BaseModel):
    name = models.CharField(verbose_name='Location Name', max_length=255)

    class Meta:
        verbose_name_plural = 'Locations'

    def __str__(self):
        return self.name


class Vacancy(BaseModel):
    name = models.CharField(verbose_name='Name', max_length=255)
    category = models.ForeignKey(verbose_name='Category', to=VacancyCategory, on_delete=models.CASCADE)
    on_site_option = models.BooleanField(verbose_name='On-Site Option', default=False)
    remote_option = models.BooleanField(verbose_name='Remote Option', default=False)
    location = models.ForeignKey(verbose_name='Location', to=Location, on_delete=models.CASCADE)
    content = RichTextField(verbose_name='Content', blank=False, null=False)
    picture = models.ImageField(verbose_name='Picture')

    class Meta:
        verbose_name_plural = 'Vacancies'

    def __str__(self):
        return self.name
