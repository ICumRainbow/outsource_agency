from django.contrib import admin

# Register your models here.
from social.models import Social


@admin.register(Social)
class SocialAdmin(admin.ModelAdmin):
    list_display = ['name']
