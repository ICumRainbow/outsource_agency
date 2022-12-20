from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.

class Work(models.Model):
    """
    Model for portfolio works.
    """
    heading = models.CharField(verbose_name='Heading', max_length=255, blank=False, null=False)
    logo = models.FileField(verbose_name='Logo')
    description = RichTextField(verbose_name='Description', blank=True, null=True)
    picture1 = models.ImageField(verbose_name='Picture 1')
    what_we_did = RichTextField(verbose_name='What We Did', blank=True, null=True)
    industry = models.CharField(verbose_name='Industry', max_length=255)
    team_size = models.IntegerField(verbose_name='Team Size', blank=True, null=True)
    location = models.CharField(verbose_name='Location', max_length=255, blank=True, null=True)
    brief = RichTextField(verbose_name='Brief', blank=False, null=True)
    approach = RichTextField(verbose_name='Approach', blank=True, null=True)
    impact = RichTextField(verbose_name='Impact', blank=True, null=True)
    metric = RichTextField(verbose_name='Metric', blank=True, null=True)
    interesting_features = RichTextField(verbose_name='Interesting Features', blank=True, null=True)
    picture2 = models.ImageField(verbose_name='Picture 2')
    what_we_built = RichTextField(verbose_name='What We Built', blank=False, null=False)
    deliverables = RichTextField(verbose_name='Deliverables', blank=False, null=False)
    picture3 = models.ImageField(verbose_name='Picture 3')
    content = RichTextField(verbose_name='Content', blank=False, null=False)

    class Meta:
        verbose_name = 'Work'
        verbose_name_plural = 'Works'

    def __str__(self):
        return self.heading
