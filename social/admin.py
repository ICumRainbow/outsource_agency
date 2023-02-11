from django.contrib import admin

from .models import Social, MainFormRequest, SecondaryFormRequest


@admin.register(Social)
class SocialAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(MainFormRequest)
class MainFormRequestAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'company', 'business_email']

@admin.register(SecondaryFormRequest)
class SecondaryFormRequestAdmin(admin.ModelAdmin):
    list_display = ['business_email']