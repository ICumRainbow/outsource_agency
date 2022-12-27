from django.db import models
from ckeditor.fields import RichTextField
from colorfield.fields import ColorField
from django.core.validators import FileExtensionValidator
# Create your models here.
from django.db.models import TextField


class Work(models.Model):
    """
    Model for portfolio works.
    """
    preview_picture = models.ImageField(blank=True, default='img_bbc_lg@2x-1.png')
    success_story_picture = models.ImageField(default='img_bbc_lg@2x-1.png')
    color = ColorField(default="#000")
    heading = models.CharField(verbose_name='Heading', max_length=255, blank=False, null=False)
    logo = models.FileField(verbose_name='Logo', validators=[FileExtensionValidator(['pdf', 'doc', 'svg'])])
    description = RichTextField(verbose_name='Description', blank=True, null=True)
    picture1 = models.ImageField(verbose_name='Picture 1')
    what_we_did = RichTextField(verbose_name='What We Did', blank=True, null=True)
    industry = models.CharField(verbose_name='Industry', max_length=255)
    team = models.CharField(verbose_name='Team', blank=True, null=True, max_length=255)
    team_size = models.IntegerField(verbose_name='Team Size', blank=True, null=True)
    location = models.CharField(verbose_name='Location', max_length=255, blank=True, null=True)
    brief = TextField(verbose_name='Brief', blank=False, null=True)
    approach = RichTextField(verbose_name='Approach', blank=True, null=True)
    impact = RichTextField(verbose_name='Impact', blank=True, null=True)
    metric = RichTextField(verbose_name='Metric', blank=True, null=True)
    interesting_features = RichTextField(verbose_name='Interesting Features', blank=True, null=True)
    picture2 = models.ImageField(verbose_name='Picture 2', blank=True)
    what_we_built = RichTextField(verbose_name='What We Built', blank=False, null=False)
    deliverables = RichTextField(verbose_name='Deliverables', blank=False, null=False)
    picture3 = models.ImageField(verbose_name='Picture 3')
    content = RichTextField(verbose_name='Content', blank=False, null=False)

    class Meta:
        verbose_name = 'Work'
        verbose_name_plural = 'Works'

    def __str__(self):
        return self.heading
