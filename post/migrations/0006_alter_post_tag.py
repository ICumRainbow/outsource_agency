# Generated by Django 4.1.4 on 2022-12-19 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0005_tag_post_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='tag',
            field=models.ManyToManyField(blank=True, to='post.tag'),
        ),
    ]