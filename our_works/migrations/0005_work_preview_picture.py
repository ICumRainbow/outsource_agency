# Generated by Django 4.1.4 on 2022-12-21 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('our_works', '0004_alter_work_options_work_color_alter_work_approach_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='work',
            name='preview_picture',
            field=models.ImageField(blank=True, default='img_bbc_lg@2x-1.png', upload_to=''),
        ),
    ]