from django.core.validators import FileExtensionValidator
from django.db import models


# Create your models here.
from core.models import BaseModel


class Social(BaseModel):
    """
    Model for Social Networks.
    """
    name = models.CharField(max_length=255)
    logo = models.FileField(verbose_name='Logo', validators=[FileExtensionValidator(['pdf', 'doc', 'svg'])])
    link = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Social'
        verbose_name_plural = 'Socials'

    def __str__(self):
        return self.name
