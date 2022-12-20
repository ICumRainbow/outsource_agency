from django.db import models


# Create your models here.

class Social(models.Model):
    """
    Model for Social Networks.
    """
    name = models.CharField(max_length=255)
    logo = models.ImageField()
    link = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Social'
        verbose_name_plural = 'Socials'

    def __str__(self):
        return self.name
