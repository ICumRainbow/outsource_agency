# Generated by Django 4.1.4 on 2022-12-20 17:36

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('our_works', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='work',
            old_name='name',
            new_name='heading',
        ),
        migrations.AddField(
            model_name='work',
            name='approach',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='work',
            name='brief',
            field=ckeditor.fields.RichTextField(null=True),
        ),
        migrations.AddField(
            model_name='work',
            name='content',
            field=ckeditor.fields.RichTextField(default=123),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='work',
            name='deliverables',
            field=ckeditor.fields.RichTextField(default=123),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='work',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='work',
            name='impact',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='work',
            name='industry',
            field=models.CharField(default=123, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='work',
            name='interesting_features',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='work',
            name='location',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='work',
            name='logo',
            field=models.ImageField(default=123, upload_to=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='work',
            name='metric',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='work',
            name='picture1',
            field=models.ImageField(default=123, upload_to=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='work',
            name='picture2',
            field=models.ImageField(default=123, upload_to=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='work',
            name='picture3',
            field=models.ImageField(default=123, upload_to=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='work',
            name='team_size',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='work',
            name='what_we_built',
            field=ckeditor.fields.RichTextField(default=123),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='work',
            name='what_we_did',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
